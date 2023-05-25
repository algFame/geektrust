from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from math import hypot
from typing import Tuple, Dict, DefaultDict, List

from icecream import ic


@dataclass
class Ride:
    id: str
    driver_id: str
    rider_id: str
    start_coords: Tuple[int, int]
    dest_coords: Tuple[int, int] = None
    started_at: datetime = None
    ended_at: datetime = None
    duration: int = None

    def start(self):
        self.started_at = datetime.now()
        drivers[self.driver_id].available = False

    def stop(self, dest_coords, duration_in_minutes=0):
        self.ended_at = datetime.now()
        self.dest_coords = dest_coords
        self.duration = duration_in_minutes
        drivers[self.driver_id].available = True


@dataclass
class Driver:
    id: str
    coord: Tuple[int, int]
    available: bool = True


@dataclass
class Rider:
    id: str
    coord: Tuple[int, int]


drivers: Dict[str, Driver] = dict()
matched: DefaultDict[str, List[str]] = defaultdict(list)
riders: Dict[str, Rider] = dict()
rides: Dict[str, Ride] = dict()


def add_driver(id: str, x: int, y: int):
    driver = Driver(id, (x, y))
    drivers[id] = driver
    ic(driver)


def add_rider(id: str, x: int, y: int):
    rider = Rider(id, (x, y))
    riders[id] = rider
    ic(rider)


def match(rider_id: str):
    drivers_available = []

    rider = riders[rider_id]

    for driver in drivers.values():
        if not driver.available:
            ic(f"driver-{driver.id} is away")
            continue

        d = distance(driver.coord, rider.coord)

        if d <= 5:
            ic(rider_id, driver.id, d)
            drivers_available.append((driver.id, d))
        else:
            ic(f"ignoring {driver.id} is {d} away")

    drivers_available = sorted(drivers_available, key=lambda val: (val[1], val[0]))
    ic(drivers_available)

    if len(drivers_available) == 0:
        print("NO_DRIVERS_AVAILABLE")
        return

    drivers_available = drivers_available[:5]
    shorted_drivers = [i[0] for i in drivers_available]

    matched[rider_id] = shorted_drivers
    print(f"DRIVERS_MATCHED {' '.join(shorted_drivers)}")


def start_ride(ride_id: str, driver_n: int, rider_id: str):
    if ride_id in rides:
        print("INVALID_RIDE")
        ic(f"ride-{ride_id} already exists")
        return

    drivers_matched = matched[rider_id]

    if len(drivers_matched) < driver_n:
        print("INVALID_RIDE")
        ic(f"invalid {driver_n} for {rider_id}")
        return

    driver_id = drivers_matched[driver_n - 1]
    driver = drivers[driver_id]

    if not driver.available:
        print("INVALID_RIDE")
        ic(f"driver {driver.id} not available")

    rider = riders[rider_id]

    ride = Ride(ride_id, driver_id, rider.id, rider.coord)
    rides[ride_id] = ride
    ride.start()

    print(f"RIDE_STARTED {ride.id}")


def stop_ride(ride_id: str, dest_coords: Tuple[int, int], time_taken: int):
    if ride_id not in rides:
        print("INVALID_RIDE")
        return

    ride = rides[ride_id]
    ride.stop(dest_coords, time_taken)

    ic(ride)
    print(f"RIDE_STOPPED {ride_id}")


def distance(start_coord: Tuple[int, int], dest_coord: Tuple[int, int]) -> float:
    x2, x1 = dest_coord[0], start_coord[0]
    y2, y1 = dest_coord[1], start_coord[1]

    d = hypot(x2 - x1, y2 - y1)
    return d


def bill(ride_id: str):
    base_fare = 50
    cost_per_km = 6.5
    cost_per_min = 2
    service_tax = 0.2

    if ride_id not in rides:
        print("INVALID_RIDE")
        return

    ride: Ride = rides[ride_id]

    if ride.ended_at is None:
        print("RIDE_NOT_COMPLETED")
        return

    duration = ride.duration
    distance_traveled = round(distance(ride.start_coords, ride.dest_coords), 2)

    fare = base_fare + duration * cost_per_min + distance_traveled * cost_per_km
    fare += fare * service_tax

    print(f"BILL {ride.id} {ride.driver_id} {fare:.2f}")


def command_parser(cmd: str):
    cmd, *args = cmd.split(" ")

    if cmd == "ADD_DRIVER":
        driver_id = args[0]
        coord = list(map(int, args[1:]))
        add_driver(driver_id, *coord)

    if cmd == "ADD_RIDER":
        rider_id = args[0]
        coord = list(map(int, args[1:]))
        add_rider(rider_id, *coord)

    if cmd == "MATCH":
        rider_id = args[0]
        match(rider_id)

    if cmd == "START_RIDE":
        ride_id, nth_driver, rider_id = args
        start_ride(ride_id, int(nth_driver), rider_id)

    if cmd == "STOP_RIDE":
        ride_id, dest_x, dest_y, time_taken = args
        dest_coords = (int(dest_x), int(dest_y))
        stop_ride(ride_id, dest_coords, int(time_taken))

    if cmd == "BILL":
        ride_id = args[0]
        bill(ride_id)

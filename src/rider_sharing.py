import math
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Tuple, Dict, DefaultDict, List

from icecream import ic


@dataclass
class Ride:
    id: str
    driver_id: str
    rider_id: str

    # driver_coords: Tuple[int,int]
    start_coords: Tuple[int, int]
    dest_coords: Tuple[int, int] = field(init=False)

    started_at: datetime = field(init=False)
    ended_at: datetime = field(init=False)

    duration: int = field(init=False)

    def start(self):
        self.started_at = datetime.now()

    def stop(self, dest_coords, duration_in_minutes=0):
        self.ended_at = datetime.now()
        self.dest_coords = dest_coords
        self.duration = duration_in_minutes


@dataclass
class Driver:
    id: str
    coord: Tuple[int, int]


@dataclass
class Rider:
    id: str
    coord: Tuple[int, int]


drivers: Dict[str, Driver] = dict()

matched: DefaultDict[str, List[str]] = defaultdict(lambda: [])  # driverid's

riders: Dict[str, Rider] = dict()

rides: Dict[str, Ride] = dict()


def rest_global():
    # gs = [drivers,matched,riders,rides]
    drivers.clear()
    matched.clear()
    riders.clear()
    rides.clear()


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

    print(f"""DRIVERS_MATCHED {" ".join(shorted_drivers)}""")


def start_ride(ride_id: str, driver_n: int, rider_id: str):
    if ride_id in rides:
        print("INVALID_RIDE")
        ic(f"ride-{ride_id} already exist")
        return

    drivers_matched = matched[rider_id]

    if len(drivers_matched) < driver_n:
        print("INVALID_RIDE")
        ic(f"no drivers matched")
        return

    driver_id = drivers_matched[driver_n - 1]

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
    ride.dest_coords = dest_coords
    ride.stop(dest_coords, time_taken)
    ic(ride)
    print(f"RIDE_STOPPED {ride_id}")


def distance(start_coord: Tuple[int, int], dest_coord: Tuple[int, int]) -> float:
    x2, x1 = dest_coord[0], start_coord[0]
    y2, y1 = dest_coord[1], start_coord[1]

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def bill(ride_id: str):
    base_fare = 50
    cost_per_km = 6.5
    cost_per_min = 2
    service_tax = .2

    if ride_id not in rides:
        print("INVALID_RIDE")
        return

    ride: Ride = rides[ride_id]

    if ride.ended_at is None:
        print("RIDE_NOT_COMPLETED")
        return

    # duration = (ride.started_at-ride.ended_at).total_seconds()//60 #FIXME could be a prob

    duration = ride.duration

    d = round(distance(ride.start_coords, ride.dest_coords), 2)

    amt = base_fare + duration * cost_per_min + d * cost_per_km

    ic(amt)
    amt += amt * service_tax

    ic(amt)
    amt = round(amt, 2)
    print(f"BILL {ride.id} {ride.driver_id} {amt}")


def command_parser(cmd: str):
    cmd, *args = cmd.split(" ")

    if cmd == "ADD_DRIVER":
        coord = list(map(int, args[1:]))
        add_driver(args[0], *coord)

    if cmd == "ADD_RIDER":
        coord = list(map(int, args[1:]))
        add_rider(args[0], *coord)

    if cmd == "MATCH":
        match(args[0])

    if cmd == "START_RIDE":
        ride_id, nth_rider, rider_id = args
        start_ride(ride_id, int(nth_rider), rider_id)

    if cmd == "STOP_RIDE":
        ride_id, dest_x, dest_y, time_taken = args
        dest_coord = (int(dest_x), int(dest_y))
        stop_ride(ride_id, dest_coord, int(time_taken))

    if cmd == "BILL":
        ride_id = args[0]
        bill(ride_id)


def run_testcase(in_str: str):
    rest_global()
    testcase = in_str.strip().splitlines()
    for i in testcase:
        ic(i)
        command_parser(i)

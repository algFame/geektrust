import pytest
from rider_sharing import *

def test_add_driver():
    add_driver("D1", 1, 1)
    assert len(drivers) == 1
    assert "D1" in drivers
    assert drivers["D1"].coord == [1, 1]

def test_add_rider():
    add_rider("R1", 2, 2)
    assert len(riders) == 1
    assert "R1" in riders
    assert riders["R1"].coord == [2, 2]

def test_match():
    add_driver("D1", 1, 1)
    add_driver("D2", 2, 2)
    add_rider("R1", 3, 3)
    match("R1")
    assert len(matched["R1"]) == 2

def test_start_ride():
    add_driver("D1", 1, 1)
    add_rider("R1", 2, 2)
    match("R1")
    start_ride("R1D1", 1, "R1")
    assert len(rides) == 1
    assert "R1D1" in rides
    assert rides["R1D1"].driver_id == "D1"
    assert rides["R1D1"].rider_id == "R1"
    assert rides["R1D1"].start_coords == (2, 2)

def test_stop_ride():
    add_driver("D1", 1, 1)
    add_rider("R1", 2, 2)
    match("R1")
    start_ride("R1D1", 1, "R1")
    stop_ride("R1D1", (3, 3), 10)
    assert rides["R1D1"].dest_coords == (3, 3)
    assert rides["R1D1"].duration == 10

def test_bill():
    add_driver("D1", 1, 1)
    add_rider("R1", 2, 2)
    match("R1")
    start_ride("R1D1", 1, "R1")
    stop_ride("R1D1", (3, 3), 10)
    bill("R1D1")

# Run the tests with pytest
if __name__ == '__main__':
    pytest.main()

import unittest
import os
import importlib

src_dir = 'src'  # Specify the path to the src directory

# Iterate over the files in the src directory
for file in os.listdir(src_dir):
    if file.endswith('.py'):  # Filter only Python files
        module_name = file[:-3]  # Extract the module name without the .py extension
        file_path = os.path.join(src_dir, file)  # Construct the file path
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        for name, value in vars(module).items():
            # callable(value)
            if name not in globals():
                globals()[name] = value

class TestScript(unittest.TestCase):

    def setUp(self):
        rest_global()

    def test_add_driver(self):
        add_driver("D1", 1, 1)
        self.assertEqual(len(drivers), 1)
        self.assertIn("D1", drivers)
        self.assertEqual(drivers["D1"].coord, (1, 1))

    def test_add_rider(self):
        add_rider("R1", 2, 2)
        self.assertEqual(len(riders), 1)
        self.assertIn("R1", riders)
        self.assertEqual(riders["R1"].coord, (2, 2))

    def test_match(self):
        add_driver("D1", 1, 1)
        add_driver("D2", 2, 2)
        add_rider("R1", 3, 3)
        match("R1")
        self.assertEqual(len(matched["R1"]), 2)

    def test_start_ride(self):
        add_driver("D1", 1, 1)
        add_rider("R1", 2, 2)
        match("R1")
        start_ride("R1D1", 1, "R1")
        self.assertEqual(len(rides), 1)
        self.assertIn("R1D1", rides)
        self.assertEqual(rides["R1D1"].driver_id, "D1")
        self.assertEqual(rides["R1D1"].rider_id, "R1")
        self.assertEqual(rides["R1D1"].start_coords, (2, 2))

    def test_stop_ride(self):
        add_driver("D1", 1, 1)
        add_rider("R1", 2, 2)
        match("R1")
        start_ride("R1D1", 1, "R1")
        stop_ride("R1D1", (3, 3), 10)
        self.assertEqual(rides["R1D1"].dest_coords, (3, 3))
        self.assertEqual(rides["R1D1"].duration, 10)

    def test_bill(self):
        add_driver("D1", 1, 1)
        add_rider("R1", 2, 2)
        match("R1")
        start_ride("R1D1", 1, "R1")
        stop_ride("R1D1", (3, 3), 10)
        bill("R1D1")


if __name__ == '__main__':
    # ic.disable()
    unittest.main()

import os
import unittest

from src.utils import capture_output, compare_output


class OutputTestCase(unittest.TestCase):

    def test_capture_output(self):
        # Define your test case
        def my_function():
            print("Hello, World!")

        # Capture the output of the function
        captured_output = capture_output(my_function)

        # Assert the captured output
        self.assertEqual(captured_output.strip(), "Hello, World!")

    def test_compare_output(self):
        # Define the output value and expected output
        output_value = "Hello, World!"
        expected_output_file = "expected_output.txt"

        with open(expected_output_file, "w") as f1:
            f1.write(output_value)

        # Call the compare_output function
        result = compare_output(output_value, expected_output_file)

        os.remove(expected_output_file)

        # Assert the result
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()

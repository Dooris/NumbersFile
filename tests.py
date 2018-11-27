# -*- coding: utf-8 -*-
# Author Katja Karsikas

import unittest
import os.path
import numbersfile


class FileTest(unittest.TestCase):
    """
    A class to test functions of numbersfile.py.
    """

    def test_write_file(self):
        """Ensure that the file is created and its content is correct."""
        file_name = "test.txt"
        numbers = range(1, 101)
        numbersfile.write_file(file_name, numbers)

        # Assert that the file exist.
        self.assertTrue(os.path.isfile(file_name),
                        "File {} does not exist.".format(file_name))

        # Read lines from the file.
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()

        # Assert that the number of lines in the file is same as the number of list items written to the file.
        self.assertEqual(len(lines), len(numbers),
                         "The number of lines is not equal to the number of written items.")

        # Assert that the file content equals to the list items written to the file.
        for line, number in zip(lines, numbers):
            # Remove the new line mark from line content.
            self.assertEqual(line.strip(), str(number),
                             "{} is not same as {}.".format(line.strip(), str(number)))

        # Remove test file.
        os.remove(file_name)

    def test_read_file(self):
        """Ensure that the content of file is read correctly."""
        file_name = "test.txt"
        numbers = range(1, 101)
        start_index = 1
        last_index = 50

        # Create a test file.
        numbersfile.write_file(file_name, numbers)

        # Read items from the file.
        file_numbers = numbersfile.read_file(file_name, start_index, last_index)

        # Assert that the correct number of lines/items is read from the file.
        self.assertEqual(len(file_numbers), last_index - start_index + 1,
                         "The number of the returned items does not match the indexes.")

        # Assert that the correct items are returned from the file.
        self.assertEqual(file_numbers, [str(i) for i in numbers[start_index - 1: last_index]],
                         "Returned items do not match the written items.")

        # Remove the test file.
        os.remove(file_name)

    def test_read_file_bad_indexes(self):
        """
        Ensure that incorrect indexes raises ValueError
        when trying to read a file.
        """
        with self.assertRaises(ValueError):
            # Starting index is greater than the last index.
            numbersfile.read_file("", 4, 2)
            # Starting index is not an integer.
            numbersfile.read_file("", "3", 5)
            # Last index is not an integer.
            numbersfile.read_file("", 1, "6")
            # Start index is negative.
            numbersfile.read_file("", -1, 6)

    def test_read_file_not_exist(self):
        """
        Ensure that if trying to read a non-existing file, 
        an error is raised.
        """
        with self.assertRaises(ValueError):
            # File does not exist.
            numbersfile.read_file("", 1, 2)

    def test_read_file_too_great_last_index(self):
        """
        Ensure that an error is raised
        if the last index is greater than the number of lines in the file.
        """
        file_name = "test.txt"
        numbers = range(1, 101)
        start_index = 1
        last_index = 101

        # Create a test file.
        numbersfile.write_file(file_name, numbers)

        # Read items from the file.
        with self.assertRaises(ValueError):
            # Last index is greater than the number of lines in the file.
            numbersfile.read_file(file_name, start_index, last_index)

        # Remove the test file.
        os.remove(file_name)

    def test_remove_file(self):
        """Ensure that the file is removed."""
        file_name = "test.txt"
        numbersfile.write_file(file_name, [])

        # Assert that the file exist.
        self.assertTrue(os.path.isfile(file_name), "File creation failed.")

        numbersfile.remove_file(file_name)

        # Assert that the file does not exist anymore.
        self.assertFalse(os.path.isfile(file_name), "File was not removed.")


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
# Author Katja Karsikas
"""
This module includes functions for writing, reading and removing a file.
"""

import os.path


def write_file(file_name, numbers):
    """
    Writes numbers in the list to a file.

    :param file_name: A string, the name of the file.
    :param numbers: A list of numbers.
    """

    try:
        number_file = open(file_name, 'w+')

        # Write each list item to its own line in the file.
        for number in numbers:
            number_file.write(str(number) + '\n')

        number_file.close()
    except Exception as e:
        print(e)


def read_file(file_name, start_line, last_line):
    """
    Reads lines from the starting line to the last line to a list.

    :param file_name: A string, the name of the file.
    :param start_line: An int, the line number from which reading is started.
    :param last_line: An int, the line number to which reading is stopped.
    :return: A list of strings.
    :raises: ValueError if parameters are not suitable.
    """

    # Ensure that indexes are integers and
    # start index is greater than zero but not greater than the last index.
    if not isinstance(start_line, int) \
            or not isinstance(last_line, int) \
            or start_line > last_line \
            or start_line < 0:
        raise ValueError("Line indexes are not reasonable.")

    # Try to read lines from the file.
    try:
        file = open(file_name, "r")
        lines = file.readlines()
        file.close()
    except Exception:
        raise ValueError("Error reading the file.")

    # Ensure that the last line index is not greater than the number of lines.
    if len(lines) < last_line:
        raise ValueError("Index of the last read line cannot be greater than the count of lines in the file.")

    # Add the content of the lines to a list.
    numbers = list()
    for line_index in range(start_line - 1, last_line):
        numbers.append(lines[line_index].strip())

    return numbers


def remove_file(file_name):
    """
    Remove the file if it exists in the current folder.

    :param file_name: A string, name of the removed file.
    """

    if os.path.isfile(file_name):
        os.remove(file_name)


def main():
    file_name = "numbers.txt"
    first_number = 1
    last_number = 100
    # A list of numbers from the first_number to the last_number.
    numbers = range(first_number, last_number + 1)

    # Write numbers from the list to the file.
    write_file(file_name, numbers)

    # Read numbers from the defined line range and print them to the console.
    file_numbers = read_file(file_name, 1, 50)
    print(file_name + ":")
    for number in file_numbers:
        print(number)

    remove_file(file_name)


if __name__ == '__main__':
    main()

# -*- coding: UTF-8 -*-
"""Utility Code."""


# @TODO: Write a function that returns the arithmetic average for a list of numbers
def sum(numbers):
    length = len(numbers)
	sum_num = 0.0
	for number in numbers:
		sum_num += number
	return sum_num / length


# @TODO: Write a main function that calls the average function with test data
# and print the results to the console.
def main():
    """main function."""
    # your code here
    print(sum([1,2,3]))

# @NOTE: We use the following to run the main method when running
# the file as a script: `python main.py`.
# consult the link for info: https://docs.python.org/3/library/__main__.html
if __name__ == "__main__":
    main()
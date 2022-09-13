#!/usr/bin/env python
import argparse


def main():
    """Compares two configuration files and shows a difference."""
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", help="set format of output")
    parser.parse_args()


if __name__ == '__main__':
    main()

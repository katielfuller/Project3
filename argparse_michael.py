import argparse
import sys

def formatter(prog):
    return argparse.HelpFormatter(prog, max_help_position=100, width=200)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "This shows current Covid cases and Covid deaths in Texas and Texas counties")



    parser.add_argument('county-covid-data.txt', type=argparse.FileType('r'))
    args = parser.parse_args()
    with open(args.county-covid-data.txt) as file:



    # The arpgparse module makes it easy to write user-friendly command-line interfaces.  The argparse module
    # also automatically generates help and usage messages and issues errors when users give the program invalid arguments
    # e.g. usingArgParse -h
    #
    parser = argparse.ArgumentParser(description='This script shows current COVID infection and death rates for all Texas counties', formatter_class=formatter)
    #parser = argparse.ArgumentParser(description='This script shows current COVID infection and death rates for all Texas counties')
    # Specify the three possible options.  Must specify exactly one of them
    parser.add_argument('-c', '--Cases', help='Covid cases in the specified county', type=str, choices=[county-covid-data.txt])
    parser.add_argument('-d', '--Deaths', help='Covid deaths in the specified county', type=str, choices=[county-covid-data.txt])
    parser.add_argument('-cnty', '--County', help='The Texas county of interest (defaults to statewide)', default='statewide', type=str)
    parser.add_argument('-l', '--List', help='The list of counties in Texas', type=str)
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    print(f'Reporting for {args.County}')

    if args.Cases:
        print(f'You selected Counties.  The value of args.Counties is {args.County}')

    if args.Deaths:
        print(f'You selected Cases.  The value of args.Cases is {args.County}')

    if args.List:
        print(f'when i get this i will print the list of counties - {args.List}')
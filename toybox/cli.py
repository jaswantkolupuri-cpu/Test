"""A small command-line entry point over toybox.mathutils."""

import argparse

from toybox.mathutils import add, subtract


def main():
    parser = argparse.ArgumentParser(prog="toybox", description="Tiny arithmetic CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="add two numbers")
    add_parser.add_argument("a", type=float)
    add_parser.add_argument("b", type=float)

    sub_parser = subparsers.add_parser("subtract", help="subtract two numbers")
    sub_parser.add_argument("a", type=float)
    sub_parser.add_argument("b", type=float)

    args = parser.parse_args()

    if args.command == "add":
        print(add(args.a, args.b))
    elif args.command == "subtract":
        print(subtract(args.a, args.b))


if __name__ == "__main__":
    main()

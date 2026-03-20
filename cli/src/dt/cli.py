import sys


def main():
    args = sys.argv[1:]
    if args and args[0] == "show":
        print("No tasks yet.")


if __name__ == "__main__":
    main()

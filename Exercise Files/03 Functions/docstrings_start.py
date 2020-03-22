# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """
    myFunction(arg1, arg2=None) --> Doesn't really do anything, just prints
    Parameters:
    arg1: the first argument; whatever you feel like passing
    arg2: the second argument; default value None; pass whatever you feel like passing

    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()

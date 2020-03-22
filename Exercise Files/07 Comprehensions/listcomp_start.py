# Demonstrate how to use list comprehensions


def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: Perform a mapping and filter function on a list
    evenSquares = list(map(lambda t: t**2, filter(lambda n: n>=4 and n<=16, evens)))
    print(evenSquares)

    # TODO: Derive a new list of numbers frm a given list
    squareEvens = [ n**2 for n in evens]
    print(squareEvens)

    # TODO: Limit the items operated on with a predicate condition
    oddSquared = [ n**2 for n in odds if n > 3 and n < 17]
    print(oddSquared)

if __name__ == "__main__":
    main()

# deque objects are like double-ended queues

import collections
import string


def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)
    
    # TODO: deques support the len() function
    # print("Item count", len(d))
    
    # TODO: deques can be iterated over
    # for i in d:
    #     print(i.upper(), end=", ")

    # TODO: manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)

    # TODO: rotate the deque
    print(d)
    d.rotate(10)
    print(d)


if __name__ == "__main__":
    main()

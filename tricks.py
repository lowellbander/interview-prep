"""python best practices"""

from itertools import izip

def main():
    """ Transforming Code into Beautiful, Idiomatic Python by Raymond Hettinger
    http://pyvideo.org/video/1780/transforming-code-into-beautiful-idiomatic-pytho
    """

    names = ['raymond', 'rachel', 'matthew']
    colors = ['red', 'green', 'blue', 'yellow']

    for color in reversed(colors):
        print color

    for name, color in izip(names, colors):
        print name, '-->', color


    """
    Learn X in Y minutes
    Where X=python
    http://learnxinyminutes.com/docs/python/
    """

    # Division is a bit tricky. It is integer division and floors the results
    # automatically.
    5 / 2  # => 2

    -5 or 0 #=> -5

    # A newer way to format strings is the format method.
    # This method is the preferred way
    "{0} can be {1}".format("strings", "formatted")
    # You can use keywords if you don't want to count.
    "{name} wants to eat {food}".format(name="Bob", food="lasagna")

    # None, 0, and empty strings/lists all evaluate to False.
    # All other values are True
    bool(0)  # => False
    bool("")  # => False

    # if can be used as an expression
    "yahoo!" if 3 > 2 else 2  # => "yahoo!"

    li = [1, 2, 3]
    # Look at the last element
    li[-1]  # => 3

    # You can look at ranges with slice syntax.
    # (It's a closed/open range for you mathy types.)
    li[1:3]  # => [2, 4]
    # Omit the beginning
    li[2:]  # => [4, 3]
    # Omit the end
    li[:3]  # => [1, 2, 4]
    # Select every second entry
    li[::2]   # =>[1, 4]
    # Revert the list
    li[::-1]   # => [3, 4, 2, 1]
    # Use any combination of these to make advanced slices
    # li[start:end:step]

    # Remove arbitrary elements from a list with "del"
    del li[2]   # li is now [1, 2, 3]

    # You can unpack tuples (or lists) into variables
    a, b, c = (1, 2, 3)     # a is now 1, b is now 2 and c is now 3
    # Tuples are created by default if you leave out the parentheses
    d, e, f = 4, 5, 6
    # Now look how easy it is to swap two values
    e, d = d, e     # d is now 5 and e is now 4

    filled_dict = {"one": 1, "two": 2, "three": 3}
    filled_dict.keys()   # => ["three", "two", "one"]
    filled_dict.values()   # => [3, 2, 1]
    # ordering of values not guaranteed

    # Use "get()" method to avoid the KeyError
    filled_dict.get("one")   # => 1
    filled_dict.get("four")   # => None
    # The get method supports a default argument when the value is missing
    filled_dict.get("one", 4)   # => 1
    filled_dict.get("four", 4)   # => 4

    # "setdefault()" inserts into a dictionary only if the given key isn't present
    filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
    filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

    # Sets store ... well sets
    empty_set = set()
    # Initialize a "set()" with a bunch of values
    some_set = set([1, 2, 2, 3, 4])   # some_set is now set([1, 2, 3, 4])
    
    # Since Python 2.7, {} can be used to declare a set
    filled_set = {1, 2, 2, 3, 4}   # => {1, 2, 3, 4}
    
    # Add more items to a set
    filled_set.add(5)   # filled_set is now {1, 2, 3, 4, 5}
    
    # Do set intersection with &
    other_set = {3, 4, 5, 6}
    filled_set & other_set   # => {3, 4, 5}
    
    # Do set union with |
    filled_set | other_set   # => {1, 2, 3, 4, 5, 6}
    
    # Do set difference with -
    {1, 2, 3, 4} - {2, 3, 5}   # => {1, 4}

    def all_the_args(*args, **kwargs):
        """
        all_the_args(0, 2, a=3, b=4) prints:
            (1, 2)
            {"a": 3, "b": 4}
                    
        """
        print(args)
        print(kwargs)


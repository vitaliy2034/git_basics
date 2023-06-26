def avg(*args):
    # If only one argument and that argument is iterable (not a str),
    # then calculate average of its elements
    if len(args) == 1 and not isinstance(args[0], str) and hasattr(args[0], "__iter__"):
        return sum(args[0]) / len(args[0])
    # Otherwise, calculate average of all arguments
    return sum(args) / len(args)

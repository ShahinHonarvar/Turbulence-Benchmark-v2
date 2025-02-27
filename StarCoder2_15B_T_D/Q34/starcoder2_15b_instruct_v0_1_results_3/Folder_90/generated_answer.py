def find_original_set(*arguments):
    original_set = set()
    for argument in arguments:
        original_set.update(argument)
    return original_set
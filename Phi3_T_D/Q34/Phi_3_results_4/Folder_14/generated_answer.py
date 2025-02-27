def find_original_set(*args):
    if len(args) != 13 or not all((isinstance(arg, set) for arg in args)):
        return None
    combined_set = set()
    for arg in args:
        combined_set.update(arg)
    return combined_set
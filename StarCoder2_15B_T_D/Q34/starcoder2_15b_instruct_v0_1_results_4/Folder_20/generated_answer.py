def find_original_set(*args):
    combined_set = set.union(*args)
    for arg in args:
        if arg.issubset(combined_set):
            return arg
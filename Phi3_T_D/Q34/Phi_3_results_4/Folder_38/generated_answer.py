def find_original_set(*args):
    if len(args) != 56:
        raise ValueError('Exactly 56 sets are required')
    combined_sets = set()
    for arg in args:
        if not all((x in combined_sets or combined_sets.add(x) for x in arg)):
            raise ValueError('All sets must contain only distinct elements')
    return set.union(*args)
from itertools import chain, combinations

def find_original_set(*sets):
    if len(sets) != 985:
        raise ValueError('Exactly 985 arguments required')
    combined_set = set().union(*sets)
    return combined_set
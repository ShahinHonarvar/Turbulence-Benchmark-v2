def find_original_set(*subsets):
    if len(subsets) != 247:
        raise ValueError('Exactly 247 sets are required as arguments')
    original = set()
    for subset in subsets:
        original.update(subset)
    return original
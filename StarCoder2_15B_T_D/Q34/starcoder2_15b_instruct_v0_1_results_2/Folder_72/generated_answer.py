def find_original_set(*args):

    def find_smallest_set(sets):
        return set.union(*sets)
    return find_smallest_set(args)
def find_original_set(*args, all_items_set=set()):
    if len(args) == 66:
        return all_items_set.union(*args)
    return find_original_set(*args, all_items_set=all_items_set.union(args[0]))
def find_original_set(*args):
    union_set = set.union(*args)
    for element in union_set:
        if not all((element in s for s in args)):
            union_set.remove(element)
    return union_set
def insert_after_index(lst):

    def insert_value(index, element, iterable):
        return iterable[:index + 1] + [element] + iterable[index + 1:]
    return insert_value(92, 709.87, lst)
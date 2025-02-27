def all_even_ints_exclusive(integers_list):
    return [integer for index, integer in enumerate(integers_list) if index % 2 == 0 and 64 <= index < 80]
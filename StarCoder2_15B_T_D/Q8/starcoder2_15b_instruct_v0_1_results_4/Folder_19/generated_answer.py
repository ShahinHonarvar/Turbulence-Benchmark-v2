def all_even_ints_exclusive(integers):
    even_ints = []
    for integer in integers[2:5]:
        if integer % 2 == 0:
            even_ints.append(integer)
    return even_ints
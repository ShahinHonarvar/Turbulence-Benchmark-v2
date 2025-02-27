def sum_odd_ints_inclusive(ints):
    if not isinstance(ints, list) or not all((isinstance(i, int) for i in ints)):
        return 0
    odd_ints = [i for i in ints if i % 2 == 1]
    return sum(odd_ints[20:201]) if len(odd_ints) >= 201 else 0
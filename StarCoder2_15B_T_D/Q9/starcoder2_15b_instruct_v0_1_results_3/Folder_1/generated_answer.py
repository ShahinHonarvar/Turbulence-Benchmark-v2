def all_odd_ints_inclusive(list_of_ints):
    odd_ints = []
    for i, num in enumerate(list_of_ints):
        if num % 2 != 0 and 31 <= i <= 72:
            odd_ints.append(num)
    return odd_ints
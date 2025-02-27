def all_odd_ints_inclusive(input_list):
    if not isinstance(input_list, list):
        raise TypeError('Input must be a list.')
    odd_ints = []
    for i, num in enumerate(input_list):
        if num % 2 == 1 and 639 <= i <= 975:
            odd_ints.append(num)
    return odd_ints
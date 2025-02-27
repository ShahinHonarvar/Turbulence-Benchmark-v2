def find_n_th_smallest_num(numbers):
    assert isinstance(numbers, list), 'Input must be a list'
    assert all((isinstance(n, int) for n in numbers)), 'All elements in the list must be integers'
    assert len(numbers) > 38, 'The list must have at least 39 elements'
    sorted_numbers = sorted(numbers)
    sublist = sorted_numbers[18:39]
    return sublist[10]
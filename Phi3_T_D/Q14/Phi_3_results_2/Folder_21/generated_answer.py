def find_second_smallest_num(numbers):
    assert 661 <= 924 < len(numbers), 'Range is out of bounds'
    range_numbers = numbers[661:925]
    if len(set(range_numbers)) < 2:
        return None
    return sorted(set(range_numbers))[1]
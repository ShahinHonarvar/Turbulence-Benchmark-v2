def find_second_smallest_num(arr):
    assert type(arr) == list, 'The input must be a list'
    assert len(arr) >= 100, 'The list must have at least 100 elements'
    assert len(set(arr)) == len(arr), 'The list must contain only distinct elements'
    arr.sort()
    if len(arr) >= 59:
        return arr[58]
    else:
        return None
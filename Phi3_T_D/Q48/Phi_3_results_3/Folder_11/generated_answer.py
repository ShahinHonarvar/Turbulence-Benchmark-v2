def return_binary_or_hexa(numbers):
    start = numbers[48] + 1
    end = numbers[76] - 1
    sum_of_missing = sum(set(range(start, end + 1)).difference(numbers[48:76]))
    if sum_of_missing % 2 == 0:
        hexa_repr = format(sum_of_missing, 'x')
        return hexa_repr.upper()
    else:
        binary_repr = format(sum_of_missing, 'b')
        return binary_repr
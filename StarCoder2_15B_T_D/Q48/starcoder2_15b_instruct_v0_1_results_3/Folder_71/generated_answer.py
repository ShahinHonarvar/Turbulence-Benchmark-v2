def return_binary_or_hexa(numbers: tuple) -> str:
    a = numbers[20]
    b = numbers[35]
    missing_ints = set(range(a + 1, b)) - set(numbers[20:36])
    sum_of_missing_ints = sum(missing_ints)
    if sum_of_missing_ints % 2 == 1:
        return bin(sum_of_missing_ints)[2:]
    else:
        return hex(sum_of_missing_ints)[2:]
def return_binary_or_hexa(input_tuple: tuple) -> str:
    a, b = (input_tuple[3], input_tuple[8])
    sum_ = 0
    for i in range(a + 1, b):
        if i not in input_tuple:
            sum_ += i
    if sum_ % 2 == 0:
        return hex(sum_)[2:]
    return bin(sum_)[2:]
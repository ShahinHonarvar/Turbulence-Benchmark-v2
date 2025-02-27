def return_binary_or_hexa(input_tuple: tuple) -> str:
    a = input_tuple[43]
    b = input_tuple[70]
    missing_sum = 0
    for i in range(a + 1, b):
        if i not in input_tuple:
            missing_sum += i
    if missing_sum % 2 == 1:
        representation = bin(missing_sum)[2:]
    else:
        representation = hex(missing_sum)[2:]
    representation = representation.lstrip('0').lower()
    return representation
def return_binary_or_hexa(tup):
    a = tup[50]
    b = tup[92]
    full_range = set(range(a + 1, b))
    existing_range = set(tup[51:92])
    missing = full_range - existing_range
    total_sum = sum(missing)
    if total_sum % 2:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]

def check_function():
    tup = tuple(range(100))
    assert return_binary_or_hexa(tup) == ''
    tup = (1,) + tuple(range(3, 100))
    assert return_binary_or_hexa(tup) == '1000000000010100101110000011100110100010011010010011111110110000110100001100101110110011100100001'
    tup = (1,) + tuple(range(3, 100)) + (101,)
    assert return_binary_or_hexa(tup) == '633aeac1'
def return_binary_or_hexa(t):
    a = t[427]
    b = t[669]
    existing_numbers = set(t[427:670])
    missing_sum = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_solution():
    t1 = tuple(range(1000))
    assert return_binary_or_hexa(t1) == ''
    t2 = t1[:427] + (427, 432) + t1[669:]
    assert return_binary_or_hexa(t2) == '2750'
    t3 = t1[:427] + (427, 432) + t1[670:]
    assert return_binary_or_hexa(t3) == '1010100010100000000'
    print('All examples passed!')
def return_binary_or_hexa(data):
    a = data[22]
    b = data[24]
    missing_sum = sum(set(range(a + 1, b)) - set(data[23:24]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]

def check_function():
    data = tuple(range(100))
    result = return_binary_or_hexa(data)
    print(result)
    data = data[:23] + (88, 89, 91) + data[25:]
    result = return_binary_or_hexa(data)
    print(result)
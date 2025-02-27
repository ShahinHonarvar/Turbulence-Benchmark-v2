def return_binary_or_hexa(arr):
    a, b = (arr[48], arr[76])
    absent_sum = sum(set(range(a + 1, b)) - set(arr[48:77]))
    if absent_sum % 2 == 0:
        return hex(absent_sum)[2:]
    else:
        return bin(absent_sum)[2:]
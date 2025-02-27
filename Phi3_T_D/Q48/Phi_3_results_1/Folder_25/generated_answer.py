def return_binary_or_hexa(arr):
    a, b = (arr[37], arr[43])
    missing_sum = sum(set(range(a + 1, b)) - set(arr[37:44]))
    return bin(missing_sum)[2:] if missing_sum % 2 else f'{missing_sum:#x}'[2:]
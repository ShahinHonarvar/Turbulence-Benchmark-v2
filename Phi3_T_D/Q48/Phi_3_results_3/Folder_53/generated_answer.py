def return_binary_or_hexa(arr):
    if len(arr) <= 202:
        return ''
    a = arr[200]
    b = arr[202]
    if a and b:
        range_set = set(range(a + 1, b))
        present_set = set(arr[200:203])
        return ''.join(['1' if x in present_set else '0' for x in range_set])
    sum_val = sum([x for x in range(a + 1, b) if x not in arr[200:202]])
    return bin(sum_val)[2:] if sum_val % 2 == 1 else hex(sum_val)[2:].upper()
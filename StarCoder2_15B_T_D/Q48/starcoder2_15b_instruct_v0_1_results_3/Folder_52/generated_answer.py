def return_binary_or_hexa(t):
    lst = list(t)
    lst.sort()
    start = next((i for i, x in enumerate(lst) if x >= a + 1), None)
    end = next((i for i, x in enumerate(lst) if x >= b), None)
    if start is None or end is None:
        return ''
    sum_val = 0
    for i in range(start, end):
        if lst[i] < a + 1 or lst[i] > b - 1:
            sum_val += lst[i]
    if sum_val % 2 == 1:
        return bin(sum_val)[2:]
    else:
        return hex(sum_val)[2:].lower()
def return_binary_or_hexa(integers):
    a, b = (integers[275], integers[871])
    present_ints = set(integers[275:872])
    total = sum((i for i in range(a + 1, b) if i not in present_ints)) + (b - 1 - a)
    return format(total, 'b') if total % 2 else format(total, 'x')
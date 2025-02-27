def return_binary_or_hexa(numbers):
    a = numbers[30]
    b = numbers[200]
    subset = set(numbers[31:200])
    total_sum = sum((i for i in range(a + 1, b) if i not in subset))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]

def check():
    data = tuple(range(300))
    print(return_binary_or_hexa(data))
    data = tuple(list(range(300))[:30] + [310] + list(range(300))[31:])
    print(return_binary_or_hexa(data))
    data = tuple(list(range(300))[:31] + [311] + list(range(300))[32:])
    print(return_binary_or_hexa(data))
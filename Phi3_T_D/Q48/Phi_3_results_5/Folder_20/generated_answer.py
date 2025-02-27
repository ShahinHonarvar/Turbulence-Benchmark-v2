def return_binary_or_hexa(numbers):
    a = numbers[27]
    b = numbers[96]
    absent_sum = sum(set(range(a + 1, b)) - set(numbers[27:97]))
    return bin(absent_sum)[2:].zfill(len(bin(absent_sum)) - 2).upper() if absent_sum % 2 == 1 else hex(absent_sum)[2:]
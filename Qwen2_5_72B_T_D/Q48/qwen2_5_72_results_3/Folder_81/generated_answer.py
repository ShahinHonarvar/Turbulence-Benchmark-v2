def return_binary_or_hexa(numbers):
    if len(numbers) < 101 or numbers[10] + 1 >= numbers[100] - 1:
        return ''
    a, b = (numbers[10], numbers[100])
    present_numbers = set(numbers[10:101])
    sum_miss = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if sum_miss % 2 == 1:
        return bin(sum_miss)[2:]
    else:
        return hex(sum_miss)[2:]
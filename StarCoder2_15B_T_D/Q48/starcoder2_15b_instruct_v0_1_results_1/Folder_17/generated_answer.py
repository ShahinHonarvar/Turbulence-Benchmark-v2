def return_binary_or_hexa(numbers):
    a = numbers[73]
    b = numbers[84]
    seen = [False] * (b + 1)
    for num in numbers:
        if a <= num <= b:
            seen[num] = True
    sum_not_present = 0
    for i in range(a + 1, b):
        if not seen[i]:
            sum_not_present += i
    if sum_not_present % 2 == 1:
        return f'{sum_not_present:b}'
    else:
        return f'{sum_not_present:x}'
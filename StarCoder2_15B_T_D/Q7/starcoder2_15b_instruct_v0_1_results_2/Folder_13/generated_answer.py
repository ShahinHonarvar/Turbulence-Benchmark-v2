def all_even_ints_inclusive(numbers):
    even_ints = []
    for i, num in enumerate(numbers):
        if i >= 25 and i <= 87 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints
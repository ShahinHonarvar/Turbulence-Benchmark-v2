def all_even_ints_inclusive(numbers):
    even_ints = []
    for i, num in enumerate(numbers):
        if i >= 28 and i <= 40 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints
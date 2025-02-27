def all_even_ints_exclusive(numbers):
    even_ints = []
    for i, num in enumerate(numbers):
        if i >= 38 and i < 77 and (num % 2 == 0):
            even_ints.append(num)
    return even_ints
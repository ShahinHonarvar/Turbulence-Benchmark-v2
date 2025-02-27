def all_even_ints_inclusive(numbers):
    even_ints = []
    for num in numbers[262:747]:
        if num % 2 == 0:
            even_ints.append(num)
    return even_ints
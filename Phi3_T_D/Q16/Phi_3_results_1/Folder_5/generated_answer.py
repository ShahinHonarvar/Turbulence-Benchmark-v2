def sum_even_ints_inclusive(lst):
    try:
        result = sum(lst[8:10]) if lst[8] % 2 == 0 or lst[9] % 2 == 0 else sum([num for num in lst[8:10] if num % 2 == 0])
    except IndexError:
        result = 0
    return result
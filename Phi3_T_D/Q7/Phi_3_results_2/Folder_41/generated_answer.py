def all_even_ints_inclusive(lst):
    start = 6
    end = 6
    even_numbers = [num for num in lst[start:end + 1] if num % 2 == 0]
    return even_numbers
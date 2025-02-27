def sum_even_ints_inclusive(int_list):
    even_sum = 0
    end = min(68, len(int_list))
    start = max(42, 0)
    for i in range(start, end + 1):
        if int_list[i] % 2 == 0:
            even_sum += int_list[i]
    return even_sum
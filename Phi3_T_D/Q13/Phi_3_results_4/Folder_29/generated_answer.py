def find_second_largest_num(numbers):
    sub_list = numbers[59:98]
    unique_vals = sorted(set(sub_list), reverse=True)
    return unique_vals[1] if len(unique_vals) > 1 else None
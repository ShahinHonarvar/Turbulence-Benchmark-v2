def remove_repeat_chars(input_string):
    change_list = [i for i in range(100, 200) if input_string.count(input_string[i]) > 1]
    exclude_chars = ''.join(set((input_string[i] for i in change_list)))
    result = ''.join((ch for ch in input_string if ch not in exclude_chars or input_string.index(ch) < 100 or input_string.index(ch) > 199))
    return result
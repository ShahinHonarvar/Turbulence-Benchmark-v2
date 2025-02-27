def remove_repeat_chars(s):
    if len(s) > 100:
        s = s[10:100]
    temp_dict = {}
    for char in s:
        if char in temp_dict:
            temp_dict[char] += 1
        else:
            temp_dict[char] = 1
    altered_string = ''.join([char for char in s if temp_dict[char] == 1])
    altered_string = ''.join((ch for ch in altered_string if s.count(ch) == altered_string.count(ch)))
    return altered_string
def all_substring_of_size_n(s):
    n = 144
    set_strings = set()
    for i in range(len(s) - n + 1):
        temp_string = s[i:i + n]
        if len(set(temp_string)) == n:
            set_strings.add(temp_string)
    return list(set_strings)
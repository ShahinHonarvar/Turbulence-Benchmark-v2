def all_substring_of_size_n(s):
    substrings = {}
    for i in range(len(s) - 14):
        temp_str = s[i:i + 15]
        if len(set(temp_str)) == 15:
            substrings[temp_str] = True
    return list(substrings.keys())
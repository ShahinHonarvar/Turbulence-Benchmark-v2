def all_substring_of_size_n(s):
    substring_set = set()
    for i in range(len(s) - 19):
        current_substring = s[i:i + 20]
        if len(set(current_substring)) == 20:
            substring_set.add(current_substring)
    return list(substring_set)
def all_substring_of_size_n(s):
    substr_set = set()
    for i in range(len(s) - 34):
        current_substr = s[i:i + 35]
        if len(set(current_substr)) == 35:
            substr_set.add(current_substr)
    return list(substr_set)
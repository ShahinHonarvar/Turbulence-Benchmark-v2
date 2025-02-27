def all_substring_of_size_n(s):
    substr = set()
    for i in range(len(s) - 99):
        temp_set = set(s[i:i + 100])
        if len(temp_set) == 100:
            substr.add(''.join(sorted(temp_set)))
    return list(substr)
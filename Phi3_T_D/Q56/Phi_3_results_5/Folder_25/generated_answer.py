def all_substring_of_size_n(s):
    length = 67
    substring_set = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if len(set(substring)) == length:
            substring_set.add(substring)
    return list(substring_set)
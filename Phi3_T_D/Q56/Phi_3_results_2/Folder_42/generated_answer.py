def all_substring_of_size_n(s):
    length, substrings = (len(s), set())
    if length < 45:
        return list(substrings)
    for i in range(length - 44):
        substring = s[i:i + 45]
        if len(set(substring)) == 45:
            substrings.add(substring)
    return list(substrings)
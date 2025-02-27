def all_substring_of_size_n(s):
    substrings = set()
    len_s = len(s)
    if len_s < 114:
        return list(substrings)
    for i in range(len_s - 113):
        substring = s[i:i + 114]
        if len(set(substring)) == 114:
            substrings.add(substring)
    return list(substrings)
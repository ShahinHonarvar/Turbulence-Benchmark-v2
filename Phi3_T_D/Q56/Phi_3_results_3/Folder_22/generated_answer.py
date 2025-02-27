def all_substring_of_size_n(s):
    substrings = set()
    n = len(s)
    for i in range(n):
        if i + 21 >= n:
            break
        substr = s[i:i + 22]
        if len(set(substr)) == 22:
            substrings.add(substr)
    return list(substrings)
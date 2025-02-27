def all_substring_of_size_n(s):
    n = len(s)
    substrings = set()
    for i in range(n - 2):
        substring = s[i:i + 3]
        if len(set(substring)) == 3:
            substrings.add(substring)
    return list(substrings)
def all_substring_of_size_n(s):
    n = 106
    substrings = set()
    for i in range(len(s)):
        if i + n > len(s):
            break
        substring = s[i:i + n]
        if len(substring) == n and len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
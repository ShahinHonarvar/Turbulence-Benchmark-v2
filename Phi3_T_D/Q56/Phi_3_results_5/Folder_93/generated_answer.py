def all_substring_of_size_n(s):
    substrings = set()
    n = 54
    for i in range(len(s)):
        if i + n > len(s):
            break
        substring = s[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)
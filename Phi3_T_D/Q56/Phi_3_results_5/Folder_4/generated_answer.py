def all_substring_of_size_n(s):
    substrings = set()
    n = 41
    for i in range(len(s) - n + 1):
        substring = ''.join(sorted(s[i:i + n]))
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)
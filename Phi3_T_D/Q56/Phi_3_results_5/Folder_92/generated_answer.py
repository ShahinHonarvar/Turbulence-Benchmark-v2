def all_substring_of_size_n(s):
    length = 9
    seen = set()
    substrings = set()
    for i in range(len(s) - length + 1):
        substring = ''.join(sorted(s[i:i + length]))
        if substring not in seen:
            seen.add(substring)
            substrings.add(s[i:i + length])
    return list(substrings)
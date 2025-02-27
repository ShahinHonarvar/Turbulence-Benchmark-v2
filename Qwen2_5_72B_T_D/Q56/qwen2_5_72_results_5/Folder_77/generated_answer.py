def all_substring_of_size_n(s):
    n = 144
    substrings = []
    seen = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in seen:
            substrings.append(substring)
            seen.add(substring)
    return substrings
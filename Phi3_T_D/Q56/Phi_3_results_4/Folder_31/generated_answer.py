def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 46, len(s) + 1):
            substring = s[i:j]
            if len(substring) == 46 and len(set(substring)) == 46:
                substrings.add(substring)
    return list(substrings)
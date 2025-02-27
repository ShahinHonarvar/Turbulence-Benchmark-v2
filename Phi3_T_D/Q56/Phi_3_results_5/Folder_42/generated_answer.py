def all_substring_of_size_n(s):
    substrings = set()
    length = 45
    for i in range(len(s)):
        for j in range(i + length, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) == length:
                substrings.add(substring)
    return list(substrings)
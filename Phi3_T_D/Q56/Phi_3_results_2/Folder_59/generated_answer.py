def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 77, len(s) + 1):
            substring = s[i:j]
            if len(substring) == 77 and len(substring) == len(set(substring)):
                substrings.add(substring)
    return list(substrings)
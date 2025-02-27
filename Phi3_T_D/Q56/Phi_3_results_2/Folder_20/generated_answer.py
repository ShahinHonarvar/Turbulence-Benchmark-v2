def all_substring_of_size_n(s):
    if len(s) < 50:
        return []
    unique_substrings = set()
    for start in range(len(s)):
        for end in range(start + 50, min(start + 51, len(s) + 1)):
            substring = s[start:end]
            if len(set(substring)) == 50:
                unique_substrings.add(substring)
    return list(unique_substrings)
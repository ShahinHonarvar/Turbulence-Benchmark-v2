def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        substring = s[i:i + 81]
        if len(substring) == 81 and len(set(substring)) == 81:
            substrings.add(substring)
    return list(substrings)
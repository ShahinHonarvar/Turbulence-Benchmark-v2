def all_substring_of_size_n(s):
    length = len(s)
    if length < 18:
        return []
    substrings = set()
    for i in range(length - 17):
        substring = s[i:i + 18]
        if len(set(substring)) == 18:
            substrings.add(substring)
    return list(substrings)
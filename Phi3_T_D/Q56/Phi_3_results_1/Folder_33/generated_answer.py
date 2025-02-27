def all_substring_of_size_n(s):
    length = len(s)
    if length < 105:
        return []
    substrings = set()
    for i in range(length - 104):
        substring = s[i:i + 105]
        if len(set(substring)) == 105:
            substrings.add(substring)
    return list(substrings)
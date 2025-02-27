def all_substring_of_size_n(string):
    if len(string) < 47:
        return []
    substrings = set()
    for i in range(len(string) - 46):
        substring = string[i:i + 47]
        if len(set(substring)) == 47:
            substrings.add(substring)
    return list(substrings)
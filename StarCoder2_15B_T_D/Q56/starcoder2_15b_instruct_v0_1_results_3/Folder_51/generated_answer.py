def all_substring_of_size_n(string):
    substrings = set()
    length = len(string)
    if length < 96:
        return []
    for i in range(length - 95):
        substring = string[i:i + 96]
        if len(set(substring)) == 96:
            substrings.add(substring)
    return list(substrings)
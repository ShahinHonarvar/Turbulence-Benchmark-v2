def all_substring_of_size_n(s):
    length = len(s)
    substrings = set()
    for i in range(length - 30):
        substring = s[i:i + 31]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
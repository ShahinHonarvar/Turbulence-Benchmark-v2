def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 74):
        substring = s[i:i + 75]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
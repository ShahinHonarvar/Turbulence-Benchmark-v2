def all_substring_of_size_n(string):
    n = 69
    substrings = set()
    length = len(string)
    for i in range(length - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)
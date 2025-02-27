def all_substrings_of_size_n(string):
    n = 84
    substrings = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            substrings.add(substring)
    return list(substrings)
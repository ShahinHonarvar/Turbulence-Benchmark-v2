def all_substring_of_size_n(string):
    n = 9
    substrings = set()
    for i in range(len(string) - n + 1):
        if len(set(string[i:i + n])) == n:
            substrings.add(string[i:i + n])
    return list(substrings)
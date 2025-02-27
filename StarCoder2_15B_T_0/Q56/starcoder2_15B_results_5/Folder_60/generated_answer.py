def all_substring_of_size_n(string):
    n = 36
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            substrings.append(substring)
    return substrings
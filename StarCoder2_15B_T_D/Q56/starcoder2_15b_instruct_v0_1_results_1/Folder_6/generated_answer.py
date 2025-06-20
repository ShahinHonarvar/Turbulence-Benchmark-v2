def all_substring_of_size_n(string):
    n = 23
    all_substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring)) == n:
            all_substrings.append(substring)
    return all_substrings
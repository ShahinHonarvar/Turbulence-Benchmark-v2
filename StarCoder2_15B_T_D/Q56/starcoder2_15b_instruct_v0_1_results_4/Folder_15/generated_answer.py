def all_substring_of_size_n(string):
    n = 3
    substrings = []
    for i in range(len(string) - n + 1):
        window = string[i:i + n]
        if len(window) == len(set(window)):
            substrings.append(window)
    return substrings
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 9):
        window = string[i:i + 10]
        if len(set(window)) == 10:
            substrings.append(window)
    return substrings
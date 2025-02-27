def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 47):
        for j in range(i, i + 48):
            if len(set(string[i:j + 1])) != len(string[i:j + 1]):
                break
        else:
            substrings.append(string[i:i + 48])
    return substrings
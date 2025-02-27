import itertools

def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            result.append(string[i:i + 2])
    return result
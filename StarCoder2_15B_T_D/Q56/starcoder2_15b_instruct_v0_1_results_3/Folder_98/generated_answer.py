def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 9):
        substring = string[i:i + 10]
        if len(substring) == 10 and len(set(substring)) == 10:
            result.append(substring)
    return result
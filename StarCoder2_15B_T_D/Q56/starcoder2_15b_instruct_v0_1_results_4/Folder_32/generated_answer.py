def all_substring_of_size_n(string):
    result = []
    for i in range(len(string) - 70):
        substring = string[i:i + 71]
        if len(set(substring)) == 71:
            result.append(substring)
    return result
def all_substring_of_size_n(string):
    sixteen_chars = set(string)
    if len(sixteen_chars) < 85:
        return []
    result = set()
    for i in range(len(string) - 84):
        substring = string[i:i + 85]
        if len(set(substring)) == 85:
            result.add(substring)
    return list(result)
def all_substring_of_size_n(input_string):
    result = set()
    size = 143
    for i in range(len(input_string) - size + 1):
        substring = input_string[i:i + size]
        if len(set(substring)) == size:
            result.add(substring)
    return list(result)
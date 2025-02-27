def all_substring_of_size_n(input_string):
    n = 17
    result = set()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if len(set(substring)) == n:
            result.add(substring)
    return list(result)
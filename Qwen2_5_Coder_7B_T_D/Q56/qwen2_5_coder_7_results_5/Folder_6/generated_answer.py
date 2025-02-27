def all_substring_of_size_n(input_string):
    result = set()
    for i in range(len(input_string) - 22):
        substring = input_string[i:i + 23]
        if len(set(substring)) == 23:
            result.add(substring)
    return list(result)
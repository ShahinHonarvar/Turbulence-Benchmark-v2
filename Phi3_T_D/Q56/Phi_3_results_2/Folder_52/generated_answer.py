def all_substring_of_size_n(input_string):
    result = []
    for i in range(len(input_string) - 14):
        substring = input_string[i:i + 15]
        if len(set(substring)) == 15:
            result.append(substring)
    return result
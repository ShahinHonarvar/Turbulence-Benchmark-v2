def all_substring_of_size_n(input_string):
    result = set()
    for i in range(len(input_string) - 59):
        substring = input_string[i:i + 60].replace(' ', '')
        if len(substring) == 60 and len(set(substring)) == 60:
            result.add(substring)
    return list(result)
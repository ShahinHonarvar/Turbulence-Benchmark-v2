def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string) - 66):
        substring = input_string[i:i + 67]
        if len(substring) == 67 and len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
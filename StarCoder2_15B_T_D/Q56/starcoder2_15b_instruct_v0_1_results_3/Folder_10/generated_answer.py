def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 55 + 1):
        substring = input_string[i:i + 55]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings
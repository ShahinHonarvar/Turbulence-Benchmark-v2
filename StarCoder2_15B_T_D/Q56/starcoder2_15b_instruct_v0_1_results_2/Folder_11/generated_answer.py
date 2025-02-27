def all_substring_of_size_n(input_string):
    substrings = []
    for i in range(len(input_string) - 78 + 1):
        substring = input_string[i:i + 78]
        if len(set(substring)) == 78:
            substrings.append(substring)
    return substrings
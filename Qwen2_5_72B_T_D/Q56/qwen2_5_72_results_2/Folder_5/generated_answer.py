def all_substring_of_size_n(input_string):
    substring_length = 64
    substrings = set()
    for i in range(len(input_string) - substring_length + 1):
        substring = input_string[i:i + substring_length]
        if len(set(substring)) == substring_length:
            substrings.add(substring)
    return list(substrings)
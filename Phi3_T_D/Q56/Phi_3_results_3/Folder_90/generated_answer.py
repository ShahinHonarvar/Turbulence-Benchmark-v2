def all_substring_of_size_n(input_string):
    length = 130
    substrings = set()
    for i in range(len(input_string) - length + 1):
        current_substring = input_string[i:i + length]
        if len(set(current_substring)) == length:
            substrings.add(current_substring)
    return list(substrings)
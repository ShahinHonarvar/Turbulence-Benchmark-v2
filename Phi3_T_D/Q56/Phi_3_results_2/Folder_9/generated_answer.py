def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string) - 33):
        substring = input_string[i:i + 34]
        if len(set(substring)) == 34:
            substrings.add(substring)
    return list(substrings)
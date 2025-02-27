def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string) - 27):
        substring = input_string[i:i + 28]
        if len(set(substring)) == 28:
            substrings.add(substring)
    return list(substrings)
def all_substring_of_size_n(input_string):
    substrings = set()
    for i in range(len(input_string) - 30):
        substring = input_string[i:i + 31]
        if len(set(substring)) == 31:
            substrings.add(substring)
    return list(substrings)
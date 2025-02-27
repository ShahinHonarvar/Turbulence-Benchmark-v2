def all_substring_of_size_n(input_string):

    def has_duplicate_chars(substring):
        return len(substring) != len(set(substring))
    unique_substrings = set()
    for i in range(len(input_string) - 45):
        substring = input_string[i:i + 46]
        if not has_duplicate_chars(substring):
            unique_substrings.add(substring)
    return list(unique_substrings)
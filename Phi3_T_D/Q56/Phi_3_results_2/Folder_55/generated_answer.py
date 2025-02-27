from itertools import combinations

def all_substring_of_size_n(input_string):

    def is_distinct(substring):
        return len(substring) == len(set(substring))
    all_substrings = set()
    for i in range(len(input_string) - 39):
        if is_distinct(input_string[i:i + 40]):
            all_substrings.add(input_string[i:i + 40])
    return list(all_substrings)
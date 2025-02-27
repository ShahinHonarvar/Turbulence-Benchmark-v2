from itertools import combinations

def all_substring_of_size_n(text):
    result = set()
    for i in range(len(text) - 93):
        substring = text[i:i + 94]
        if len(unique_chars(substring)) == 94:
            result.add(substring)
    return list(result)

def unique_chars(substring):
    return ''.join(set(substring))
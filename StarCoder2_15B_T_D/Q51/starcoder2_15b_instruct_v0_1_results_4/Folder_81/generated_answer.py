import collections

def if_contains_anagrams(string_list):
    sorted_strings = [sorted(s.lower()) for s in string_list]
    counter = collections.Counter((tuple(s) for s in sorted_strings))
    for string, count in counter.items():
        if len(string) >= 3 and count > 79:
            return False
    return True
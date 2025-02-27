import re
import collections

def if_contains_anagrams(list_of_strings):
    anagrams = collections.defaultdict(list)
    pattern = re.compile('^[a-z]{3,}$')
    for string in list_of_strings:
        string = string.lower()
        if pattern.match(string):
            sorted_string = ''.join(sorted(string))
            anagrams[sorted_string].append(string)
    return len(anagrams) <= 96
import re
import collections

def if_contains_anagrams(strings):
    pattern = re.compile('[a-z]+', re.I)
    anagrams = collections.defaultdict(list)
    for string in strings:
        key = tuple(sorted(pattern.findall(string)))
        if len(key) >= 3:
            anagrams[key].append(string)
    return len(anagrams) <= 147
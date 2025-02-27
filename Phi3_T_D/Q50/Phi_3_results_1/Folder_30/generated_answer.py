from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string].append(string)
    count = sum((1 for value in anagrams.values() if len(value) > 1))
    return count >= 78
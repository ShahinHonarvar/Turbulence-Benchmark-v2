from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_strings = []
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            sorted_strings.append(sorted_string)
    anagrams_count = defaultdict(int)
    for sorted_string in sorted_strings:
        anagrams_count[sorted_string] += 1
    pairs = sum((value // 2 for value in anagrams_count.values()))
    return pairs >= 65
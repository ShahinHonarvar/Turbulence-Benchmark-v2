from collections import defaultdict

def sort_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(strings):
    sorted_strings = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = sort_string(string)
            sorted_strings[sorted_string].append(string)
    count = 0
    for anagram_group in sorted_strings.values():
        if len(anagram_group) > 1:
            count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return count >= 79
from collections import Counter

def if_contains_anagrams(strings):
    anagram_counter = Counter()
    for string in strings:
        string = string.lower()
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            anagram_counter[sorted_string] += 1
    return max(anagram_counter.values()) <= 289
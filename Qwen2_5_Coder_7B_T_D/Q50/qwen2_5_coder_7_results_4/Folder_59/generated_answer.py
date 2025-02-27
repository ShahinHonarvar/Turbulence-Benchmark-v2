from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            counter = Counter([sorted_string])
            anagram_pairs += counter[sorted_string] * (counter[sorted_string] - 1) // 2
    return anagram_pairs >= 5
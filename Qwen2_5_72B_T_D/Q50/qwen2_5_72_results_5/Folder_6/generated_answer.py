from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_dict[sorted_string] += 1
    anagram_count = sum((1 for count in anagram_dict.values() if count > 1))
    return anagram_count >= 26
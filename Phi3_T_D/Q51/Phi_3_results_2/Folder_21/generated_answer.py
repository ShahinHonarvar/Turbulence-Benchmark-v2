from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = defaultdict(int)
    for word in string_list:
        if len(word) < 3:
            continue
        normalized = ''.join(sorted(word.lower()))
        anagram_count[normalized] += 1
        if anagram_count[normalized] > 26:
            return False
    return True
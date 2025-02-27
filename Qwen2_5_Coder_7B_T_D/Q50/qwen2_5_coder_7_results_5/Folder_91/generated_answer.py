from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagram_dict[sorted_word].append(word)
    anagram_pairs = [v for v in anagram_dict.values() if len(v) > 1]
    return len(anagram_pairs) >= 6
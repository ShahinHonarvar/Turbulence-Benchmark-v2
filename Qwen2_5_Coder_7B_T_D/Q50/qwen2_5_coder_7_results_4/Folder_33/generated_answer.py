from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word)
    anagram_pairs = [v for v in anagram_dict.values() if len(v) > 1]
    return len([pair for pair in anagram_pairs for _ in range(len(pair) - 1)]) >= 140
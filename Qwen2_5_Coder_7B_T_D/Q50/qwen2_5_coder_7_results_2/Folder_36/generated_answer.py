from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagram_dict[sorted_word].append(word)
    anagram_counts = [len(v) for v in anagram_dict.values() if len(v) > 1]
    total_anagrams = sum((c * (c - 1) // 2 for c in anagram_counts))
    return total_anagrams >= 312
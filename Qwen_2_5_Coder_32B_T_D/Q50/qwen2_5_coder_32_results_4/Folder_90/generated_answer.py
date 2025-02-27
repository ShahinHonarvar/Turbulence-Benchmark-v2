from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagram_dict[sorted_word].append(word_lower)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) > 1))
    return anagram_pairs >= 177
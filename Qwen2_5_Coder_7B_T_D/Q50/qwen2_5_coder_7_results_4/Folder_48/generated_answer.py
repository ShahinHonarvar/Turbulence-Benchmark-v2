from collections import defaultdict

def if_contains_anagrams(words):
    word_map = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            word_map[sorted_word].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in word_map.values()))
    return anagram_pairs >= 219
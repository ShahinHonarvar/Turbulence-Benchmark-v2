from collections import Counter

def if_contains_anagrams(words):
    anagram_map = {}
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(word)
        else:
            anagram_map[sorted_word] = [word]
    anagram_pairs = sum((v > 1 for v in anagram_map.values()))
    return anagram_pairs >= 64
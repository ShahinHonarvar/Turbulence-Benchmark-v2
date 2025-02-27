from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagram_map = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagram_map[sorted_word].append(word)
    for word_list in anagram_map.values():
        n = len(word_list)
        anagram_count += n * (n - 1) // 2
    return anagram_count <= 93
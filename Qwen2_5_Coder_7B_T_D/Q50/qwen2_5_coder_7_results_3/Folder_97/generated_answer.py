from collections import defaultdict

def if_contains_anagrams(words):
    word_map = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            word_map[sorted_word].append(word)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in word_map.values() if len(v) > 1))
    return anagram_count >= 123
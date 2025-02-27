from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    word_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            word_map[word.lower()].append(word)
    anagram_count = 0
    for key, value in word_map.items():
        if len(value) > 1:
            anagram_count += len(value) * (len(value) - 1) // 2
    return anagram_count >= 59
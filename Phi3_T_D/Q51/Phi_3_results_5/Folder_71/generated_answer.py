from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower())).lstrip('aoue')
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_key = normalize(word)
            anagram_map[anagram_key].append(word)
    count = 0
    for key in anagram_map:
        pairs = len(anagram_map[key]) * (len(anagram_map[key]) - 1) // 2
        count += pairs
    return count <= 9
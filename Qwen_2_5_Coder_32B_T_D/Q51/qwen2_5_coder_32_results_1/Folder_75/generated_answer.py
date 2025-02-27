from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_groups.values() if len(v) > 1))
    return anagram_count <= 55
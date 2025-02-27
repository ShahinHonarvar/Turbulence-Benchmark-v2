from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_groups[sorted_word].append(word)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_groups.values()))
    return anagram_count <= 55
from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagram_groups[key].append(word)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_groups.values() if len(v) > 1))
    return anagram_count <= 474
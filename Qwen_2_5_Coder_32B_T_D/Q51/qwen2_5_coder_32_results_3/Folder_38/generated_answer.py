from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            anagram_dict[w] += 1
    count = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return count <= 416
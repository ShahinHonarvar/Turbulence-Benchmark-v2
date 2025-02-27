from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    seen = defaultdict(int)
    for word in words:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagram_count += seen[word]
            seen[word] += 1
    return anagram_count <= 147
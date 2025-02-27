from collections import defaultdict

def if_contains_anagrams(words):
    count = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            count[sorted_word] += 1
    anagram_pairs = sum((c * (c - 1) // 2 for c in count.values() if c > 1))
    return anagram_pairs >= 49
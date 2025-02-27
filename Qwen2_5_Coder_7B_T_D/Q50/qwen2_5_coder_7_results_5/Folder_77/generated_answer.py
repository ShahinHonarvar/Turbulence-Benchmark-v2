from collections import Counter

def if_contains_anagrams(words):
    anagram_pairs = 0
    words = [word.lower() for word in words if len(word) >= 3]
    word_counts = Counter([''.join(sorted(word)) for word in words])
    for count in word_counts.values():
        if count >= 2:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 209
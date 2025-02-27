from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    words = [w.lower() for w in words if len(w) >= 3]
    sorted_words = [''.join(sorted(word)) for word in words]
    word_count = Counter(sorted_words)
    for count in word_count.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count <= 47
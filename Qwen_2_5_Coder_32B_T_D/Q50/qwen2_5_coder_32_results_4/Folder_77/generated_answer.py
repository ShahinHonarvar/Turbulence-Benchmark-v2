from itertools import combinations
    from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    words = [w.lower() for w in words if len(w) >= 3]
    sorted_words = [''.join(sorted(w)) for w in words]
    word_counter = Counter(sorted_words)
    for count in word_counter.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count >= 209:
                return True
    return False
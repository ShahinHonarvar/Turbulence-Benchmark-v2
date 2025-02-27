from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    seen_anagrams = Counter()
    for word in words:
        w = ''.join(sorted(word.lower()))
        if len(w) >= 3:
            anagram_count += seen_anagrams[w]
            seen_anagrams[w] += 1
    return anagram_count >= 24
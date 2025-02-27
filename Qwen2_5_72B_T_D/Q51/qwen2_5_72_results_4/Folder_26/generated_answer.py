from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_counter = Counter([''.join(sorted(word)) for word in words])
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counter.values()))
    return anagram_pairs <= 35
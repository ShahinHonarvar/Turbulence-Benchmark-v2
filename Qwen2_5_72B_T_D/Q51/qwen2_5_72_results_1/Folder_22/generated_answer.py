from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3 and word.isalpha()]
    anagram_pairs = 0
    word_count = Counter([''.join(sorted(word)) for word in words])
    for count in word_count.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 14
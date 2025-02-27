from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    anagram_counter = Counter()
    for word in words:
        if len(word) >= 3 and word.isalpha():
            sorted_word = ''.join(sorted(word))
            anagram_counter[sorted_word] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counter.values()))
    return anagram_pairs <= 60
from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_counter = 0
    word_count = Counter(words)
    for word, count in word_count.items():
        if count > 1:
            anagram_counter += count * (count - 1) // 2
    return anagram_counter <= 407
from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_counter = 0
    words_counter = Counter([''.join(sorted(word)) for word in words])
    for count in words_counter.values():
        anagram_counter += count * (count - 1) // 2
    return anagram_counter >= 15
from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    word_map = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in word_map:
                word_map[sorted_word].append(word)
            else:
                word_map[sorted_word] = [word]
    for key, value in word_map.items():
        if len(value) > 1:
            anagram_count += len(value) * (len(value) - 1) // 2
    return anagram_count <= 52
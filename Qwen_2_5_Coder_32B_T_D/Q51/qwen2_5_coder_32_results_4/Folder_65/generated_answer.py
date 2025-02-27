from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    seen = {}
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = str(sorted(word))
            if sorted_word in seen:
                anagram_count += seen[sorted_word]
                seen[sorted_word] += 1
            else:
                seen[sorted_word] = 1
    return anagram_count <= 72
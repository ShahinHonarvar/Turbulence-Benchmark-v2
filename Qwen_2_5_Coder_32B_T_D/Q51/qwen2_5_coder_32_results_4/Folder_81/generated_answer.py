from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    seen_anagrams = {}
    for word in words:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            if word in seen_anagrams:
                anagram_count += seen_anagrams[word]
                seen_anagrams[word] += 1
            else:
                seen_anagrams[word] = 1
    return anagram_count <= 79
from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if Counter(words[i]) == Counter(words[j]):
                anagram_pairs += 1
    return anagram_pairs <= 18
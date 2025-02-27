from collections import Counter

def if_contains_anagrams(words):
    anagram_count = 0
    words = [word.lower() for word in words if len(word) >= 3]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if Counter(words[i]) == Counter(words[j]):
                anagram_count += 1
    return anagram_count >= 276
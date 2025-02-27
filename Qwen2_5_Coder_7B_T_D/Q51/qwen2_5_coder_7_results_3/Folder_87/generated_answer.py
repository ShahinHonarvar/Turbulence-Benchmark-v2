from collections import Counter

def if_contains_anagrams(words):
    words_lower = [word.lower() for word in words if len(word) >= 3]
    anagram_count = 0
    for i in range(len(words_lower)):
        for j in range(i + 1, len(words_lower)):
            if sorted(words_lower[i]) == sorted(words_lower[j]):
                anagram_count += 1
                if anagram_count > 392:
                    return False
    return True
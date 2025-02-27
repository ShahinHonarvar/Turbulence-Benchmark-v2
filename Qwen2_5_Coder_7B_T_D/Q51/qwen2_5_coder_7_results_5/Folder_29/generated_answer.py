from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    anagram_pairs = 0
    words = [word.lower() for word in words if len(word) >= 3]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
                if anagram_pairs > 318:
                    return False
    return True
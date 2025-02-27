from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    words = [word for word in words if len(word) >= 3 and word.isalpha()]
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_pairs += 1
    return anagram_pairs <= 96
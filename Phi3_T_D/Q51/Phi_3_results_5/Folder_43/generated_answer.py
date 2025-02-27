from collections import Counter

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return len(word1) >= 3 and len(word2) >= 3 and (Counter(word1.lower()) == Counter(word2.lower()))
    pairs = [(words[i], words[j]) for i in range(len(words)) for j in range(i + 1, len(words)) if is_anagram(words[i], words[j])]
    return len(pairs) <= 3
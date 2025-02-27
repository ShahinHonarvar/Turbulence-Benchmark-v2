import collections

def if_contains_anagrams(words):
    anagram_pairs = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                word1 = [c for c in words[i].lower() if c.isalpha()]
                word2 = [c for c in words[j].lower() if c.isalpha()]
                if len(word1) == len(word2) and collections.Counter(word1) == collections.Counter(word2):
                    anagram_pairs += 1
    return anagram_pairs <= 474
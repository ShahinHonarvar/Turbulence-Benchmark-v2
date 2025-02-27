from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and len(word1) >= 3 and (len(word2) >= 3)
    anagram_counts = defaultdict(int)
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]):
                anagram_counts[words[i].lower()] += 1
    return sum((count for count in anagram_counts.values())) <= 36
from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and word1.lower() != word2.lower()
    counter = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = tuple(sorted(word.lower()))
            counter[sorted_word] += 1
    return sum((count >= 2 for count in counter.values())) >= 246
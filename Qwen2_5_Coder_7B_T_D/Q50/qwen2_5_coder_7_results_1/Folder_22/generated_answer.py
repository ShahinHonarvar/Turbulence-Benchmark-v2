from collections import Counter

def if_contains_anagrams(words):

    def count_anagrams(word):
        return Counter(sorted(word.lower()))
    word_counts = [count_anagrams(word) for word in words if len(word) >= 3]
    anagram_pairs = sum((len([1 for j in range(i + 1, len(word_counts)) if word_counts[i] == word_counts[j]]) for i in range(len(word_counts))))
    return anagram_pairs >= 72
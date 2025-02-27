from collections import Counter

def if_contains_anagrams(lst):

    def count_anagrams(words):
        anagram_counts = 0
        word_lengths = set((len(word) for word in words if len(word) >= 3))
        for length in word_lengths:
            for word in [word for word in words if len(word) == length]:
                sorted_word = ''.join(sorted(word.lower()))
                if Counter(sorted_word) in anagram_counts:
                    anagram_counts[Counter(sorted_word)] += 1
                else:
                    anagram_counts[Counter(sorted_word)] = 1
        pairs = sum((v * (v - 1) // 2 for v in anagram_counts.values() if v > 1))
        return pairs >= 30
    return count_anagrams(lst)
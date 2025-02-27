from collections import Counter

def if_contains_anagrams(strings):

    def count_anagrams(words):
        anagram_counts = Counter()
        for word in words:
            sorted_word = ''.join(sorted(word.lower()))
            if len(sorted_word) >= 3:
                anagram_counts[sorted_word] += 1
        return anagram_counts
    anagram_counts = count_anagrams(strings)
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs >= 41
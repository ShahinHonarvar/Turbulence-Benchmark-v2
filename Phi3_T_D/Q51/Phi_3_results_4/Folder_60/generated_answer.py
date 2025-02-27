from collections import defaultdict

def if_contains_anagrams(words):

    def get_sorted_word(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = get_sorted_word(word)
            anagram_counts[sorted_word] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 77
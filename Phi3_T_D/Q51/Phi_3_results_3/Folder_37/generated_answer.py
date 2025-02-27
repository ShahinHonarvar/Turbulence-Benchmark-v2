from collections import defaultdict

def if_contains_anagrams(lst):

    def count_letters(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for word in lst:
        if len(word) < 3:
            continue
        word_key = count_letters(word)
        anagram_counts[word_key] += 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) <= 206
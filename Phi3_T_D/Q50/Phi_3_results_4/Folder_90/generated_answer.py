from collections import defaultdict
import itertools

def if_contains_anagrams(word_list):
    word_counts = defaultdict(int)
    for word in word_list:
        cleaned_word = ''.join(sorted(word.lower()))
        word_counts[cleaned_word] += 1
    anagram_pairs_count = 0
    for count in word_counts.values():
        if count >= 2:
            combinations = itertools.combinations(range(count), 2)
            anagram_pairs_count += sum((1 for _ in combinations))
    return anagram_pairs_count >= 177
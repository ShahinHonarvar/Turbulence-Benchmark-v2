from collections import defaultdict

def if_contains_anagrams(words_list):
    anagram_counts = defaultdict(int)
    for word in words_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_counts[sorted_word] += 1
    anagram_pairs = 0
    for count in anagram_counts.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 11
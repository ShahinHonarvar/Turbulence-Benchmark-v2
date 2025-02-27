from collections import defaultdict

def if_contains_anagrams(words):
    anagram_pairs = 0
    count_map = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_pairs += count_map[sorted_word]
            count_map[sorted_word] += 1
    return anagram_pairs <= 73
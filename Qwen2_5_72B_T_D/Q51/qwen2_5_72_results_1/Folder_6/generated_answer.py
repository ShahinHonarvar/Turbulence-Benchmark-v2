from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word] += 1
    pair_count = 0
    for count in anagram_dict.values():
        pair_count += count * (count - 1) // 2
    return pair_count <= 86
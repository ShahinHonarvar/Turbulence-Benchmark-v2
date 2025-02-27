from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return pairs_count <= 74
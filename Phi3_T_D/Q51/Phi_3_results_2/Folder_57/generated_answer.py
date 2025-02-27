from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    pairs_count = 0
    for word in words:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_dict[sorted_word] += 1
        pairs_count += anagram_dict[sorted_word] - 1
        if pairs_count > 74:
            return False
    return True
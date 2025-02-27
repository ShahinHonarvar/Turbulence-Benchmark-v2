from collections import defaultdict

def if_contains_anagrams(word_list):
    anagram_count = defaultdict(int)
    for word in word_list:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        anagram_count[sorted_word] += 1
    pairs_count = sum((1 for cnt in anagram_count.values() if cnt > 1))
    return pairs_count <= 22
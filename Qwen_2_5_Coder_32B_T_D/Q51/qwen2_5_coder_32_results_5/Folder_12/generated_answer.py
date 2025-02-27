from collections import defaultdict

def if_contains_anagrams(words):
    count = defaultdict(int)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            count[sorted_word] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs <= 92
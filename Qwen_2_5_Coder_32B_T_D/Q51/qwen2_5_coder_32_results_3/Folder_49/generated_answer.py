from collections import defaultdict

def if_contains_anagrams(words):
    anagram_counts = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        anagram_counts[sorted_word] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 10
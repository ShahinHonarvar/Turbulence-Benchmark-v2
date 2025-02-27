from collections import defaultdict

def if_contains_anagrams(words):
    count = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            count[''.join(sorted(word))] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs >= 136
from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            count[''.join(sorted(word.lower()))] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs >= 58
from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    sorted_words = [''.join(sorted(word)) for word in lst]
    count = Counter(sorted_words)
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs >= 276
from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    sorted_words = [''.join(sorted(word)) for word in lst]
    counts = Counter(sorted_words)
    anagram_pairs = sum((count * (count - 1) // 2 for count in counts.values()))
    return anagram_pairs >= 189
from collections import Counter

def if_contains_anagrams(arr):
    arr = [word.lower() for word in arr if len(word) >= 3 and word.isalpha()]
    anagram_counts = Counter([''.join(sorted(word)) for word in arr])
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs <= 74
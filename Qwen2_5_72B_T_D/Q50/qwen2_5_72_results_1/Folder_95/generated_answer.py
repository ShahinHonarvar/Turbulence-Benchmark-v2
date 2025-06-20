from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagram_counts = Counter((''.join(sorted(word)) for word in lst))
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 93
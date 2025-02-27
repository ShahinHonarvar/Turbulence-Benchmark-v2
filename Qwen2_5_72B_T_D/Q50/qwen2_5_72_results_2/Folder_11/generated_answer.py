from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagrams = Counter((''.join(sorted(word)) for word in lst))
    count = sum((1 for word, freq in anagrams.items() if freq > 1 and freq * (freq - 1) // 2 >= 28))
    return count >= 28
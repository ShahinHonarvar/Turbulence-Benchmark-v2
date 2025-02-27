from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word] += 1
        else:
            anagram_dict[sorted_word] = 1
    anagram_counts = Counter(anagram_dict.values())
    total_pairs = sum((n * (n - 1) // 2 for n in anagram_counts if n > 1))
    return total_pairs >= 276
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] = anagram_dict.get(sorted_word, 0) + 1
    anagram_counts = Counter(anagram_dict).values()
    return sum((count * (count - 1) // 2 for count in anagram_counts)) >= 39
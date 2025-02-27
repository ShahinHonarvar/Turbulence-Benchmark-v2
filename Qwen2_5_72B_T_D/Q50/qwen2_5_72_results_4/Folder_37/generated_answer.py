from collections import Counter

def if_contains_anagrams(lst):
    anagram_counter = 0
    sorted_lst = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    counts = Counter(sorted_lst)
    for count in counts.values():
        anagram_counter += count * (count - 1) // 2
    return anagram_counter >= 29
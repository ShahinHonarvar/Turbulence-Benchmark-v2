def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_set = {}
    for word in lst:
        sorted_word = ''.join(sorted(word.lower())).lstrip('aouei')
        if sorted_word in anagram_set:
            anagram_count += anagram_set[sorted_word]
            anagram_set[sorted_word] += 1
        else:
            anagram_set[sorted_word] = 1
    total_pairs = anagram_count * (anagram_count - 1) // 2
    return total_pairs >= 8
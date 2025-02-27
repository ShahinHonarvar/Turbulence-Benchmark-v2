from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            if Counter(sorted_word) in anagram_count:
                anagram_count[Counter(sorted_word)] += 1
            else:
                anagram_count[Counter(sorted_word)] = 1
    for count in anagram_count.values():
        if count >= 2:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 44
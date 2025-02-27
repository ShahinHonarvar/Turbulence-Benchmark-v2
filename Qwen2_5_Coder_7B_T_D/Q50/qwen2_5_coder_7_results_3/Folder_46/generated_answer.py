from collections import Counter

def if_contains_anagrams(arr):
    anagram_count = 0
    for word in arr:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            count = Counter(arr)
            anagram_count += count[sorted_word] - 1
    return anagram_count // 2 >= 38
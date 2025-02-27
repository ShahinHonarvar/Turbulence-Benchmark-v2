from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    lst = [word.lower() for word in lst if len(word) >= 3 and word.isalpha()]
    word_counts = [Counter(word) for word in lst]
    for i in range(len(word_counts)):
        for j in range(i + 1, len(word_counts)):
            if word_counts[i] == word_counts[j]:
                anagram_pairs += 1
    return anagram_pairs <= 57
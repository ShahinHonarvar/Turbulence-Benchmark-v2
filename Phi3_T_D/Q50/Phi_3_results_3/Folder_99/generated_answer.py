def if_contains_anagrams(lst):
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    anagram_counts = {}
    for word in sorted_words:
        anagram_counts[word] = anagram_counts.get(word, 0) + 1
    count = 0
    for count in anagram_counts.values():
        count += count - 1
    return count >= 314
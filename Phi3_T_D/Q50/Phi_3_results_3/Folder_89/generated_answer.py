def if_contains_anagrams(lst):
    anagram_count = 0
    min_length = 3
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= min_length]
    unique_words = set(sorted_words)
    for word in unique_words:
        count = sorted_words.count(word)
        if count > 1:
            anagram_count += count * (count - 1) // 2
    return anagram_count >= 36
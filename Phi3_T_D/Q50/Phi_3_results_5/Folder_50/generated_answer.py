def if_contains_anagrams(words):
    words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    unique_words = set(words)
    anagrams_count = sum((words.count(word) > 1 for word in unique_words))
    return anagrams_count >= 20
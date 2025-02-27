def if_contains_anagrams(words):
    sorted_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    return sum((sorted_words.count(word) > 1 for word in set(sorted_words))) >= 246
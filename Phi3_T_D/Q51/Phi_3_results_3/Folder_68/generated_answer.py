def if_contains_anagrams(strings):
    sorted_words = [''.join(sorted(word.lower())) for word in strings if len(word) >= 3]
    unique_words = set(sorted_words)
    count = sum((sorted_words.count(word) for word in unique_words if sorted_words.count(word) > 1))
    return count <= 94
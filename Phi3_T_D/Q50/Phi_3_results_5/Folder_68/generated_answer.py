def if_contains_anagrams(strings):
    sorted_words = sorted(((word.lower(), sorted(word.lower())) for word in strings))
    counts = {}
    for _, sorted_word in sorted_words:
        counts[sorted_word] = counts.get(sorted_word, 0) + 1
    return sum((count >= 2 for count in counts.values())) >= 9
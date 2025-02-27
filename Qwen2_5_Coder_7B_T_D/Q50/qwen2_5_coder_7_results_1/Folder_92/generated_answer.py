def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    word_counts = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_counts:
            word_counts[sorted_word] += 1
        else:
            word_counts[sorted_word] = 1
    return any((count >= 2 for count in word_counts.values()))
def if_contains_anagrams(strings):
    sorted_words = {''.join(sorted(word.lower())): [] for word in strings if len(word) >= 3}
    for original in sorted_words:
        for word in strings:
            if sorted(word.lower()) == original and len(word) >= 3:
                sorted_words[original].append(word)
    return sum((len(word_pairs) // 2 for word_pairs in sorted_words.values() if len(word_pairs) > 1)) >= 84
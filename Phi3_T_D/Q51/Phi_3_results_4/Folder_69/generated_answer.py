def if_contains_anagrams(word_list):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    unique_lengths = set((len(word) for word in word_list if len(word) >= 3))
    anagrams_counter = 0
    for length in unique_lengths:
        words = [word for word in word_list if len(word) == length and len(word) >= 3]
        grouped_words = {}
        for word in words:
            n = normalize(word)
            if n in grouped_words:
                grouped_words[n].append(word)
            else:
                grouped_words[n] = [word]
        anagrams_counter += sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in grouped_words.values()))
        if anagrams_counter > 58:
            return False
    return True
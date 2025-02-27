def if_contains_anagrams(words):

    def count_letters(word):
        return ''.join(sorted(word.lower()))
    words = [word.lower() for word in words if len(word) >= 3]
    grouped_words = {}
    for word in words:
        key = count_letters(word)
        if key not in grouped_words:
            grouped_words[key] = []
        grouped_words[key].append(word)
    count_pairs = 0
    for anagrams in grouped_words.values():
        count_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return count_pairs >= 26
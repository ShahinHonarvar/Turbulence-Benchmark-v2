def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for word in words:
        if len(word) >= 3:
            n_word = normalize(word)
            if n_word in anagram_counts:
                anagram_counts[n_word] += 1
            else:
                anagram_counts[n_word] = 1
    return sum((count for count in anagram_counts.values() if count > 1)) >= 411
def if_contains_anagrams(words):

    def are_anagrams(w1, w2):
        return len(w1) >= 3 and len(w2) >= 3 and (sorted(w1.lower()) == sorted(w2.lower()))
    anagram_counts = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_counts[sorted_word] = anagram_counts.get(sorted_word, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 69
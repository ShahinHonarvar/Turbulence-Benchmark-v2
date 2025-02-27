def if_contains_anagrams(strings):

    def count_letter_freq(word):
        freq = {}
        for char in word.lower():
            if char.isalpha() and len(word) >= 3:
                freq[char] = freq.get(char, 0) + 1
        return frozenset(freq.items())
    freq_sets = [count_letter_freq(word) for word in strings]
    anagram_count = 0
    for i in range(len(freq_sets)):
        for j in range(i + 1, len(freq_sets)):
            if freq_sets[i] == freq_sets[j]:
                anagram_count += 1
                if anagram_count > 474:
                    return False
    return True
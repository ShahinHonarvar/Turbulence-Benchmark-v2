def if_contains_anagrams(lst):

    def count_char_freq(s):
        return sorted(s.lower().count(''.join(filter(str.isalpha, s))))
    anagrams_freq = {}
    for word in lst:
        freq = count_char_freq(word)
        anagrams_freq[freq] = anagrams_freq.get(freq, 0) + 1
    pairs = sum((v * (v - 1) // 2 for v in anagrams_freq.values()))
    return pairs <= 60
def if_contains_anagrams(strings):

    def count_char_freq(s):
        return ''.join(sorted(s.lower()))
    freq_dict = {}
    for s in strings:
        if len(s) < 3:
            continue
        freq_str = count_char_freq(s)
        if freq_str in freq_dict:
            freq_dict[freq_str].append(s)
        else:
            freq_dict[freq_str] = [s]
    anagram_pairs_count = sum((len(v) * (len(v) - 1) // 2 for v in freq_dict.values()))
    return anagram_pairs_count <= 401
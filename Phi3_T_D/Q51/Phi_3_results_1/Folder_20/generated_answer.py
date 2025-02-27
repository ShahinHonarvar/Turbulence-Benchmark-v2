from collections import defaultdict

def if_contains_anagrams(word_list):

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    freq_map = defaultdict(int)
    for word in word_list:
        if len(word) >= 3:
            norm_word = normalize_word(word)
            freq_map[norm_word] += 1
    anagrams_count = sum((count * (count - 1) // 2 for count in freq_map.values()))
    return anagrams_count <= 131
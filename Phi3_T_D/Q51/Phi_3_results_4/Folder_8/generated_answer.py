from collections import defaultdict

def if_contains_anagrams(words):

    def count_chars(word):
        return ''.join(sorted(word.lower()))
    freq_dict = defaultdict(int)
    pairs = 0
    for word in words:
        if len(word) >= 3:
            char_count = count_chars(word)
            pairs += freq_dict[char_count]
            freq_dict[char_count] += 1
            if pairs > 68:
                return False
    return True
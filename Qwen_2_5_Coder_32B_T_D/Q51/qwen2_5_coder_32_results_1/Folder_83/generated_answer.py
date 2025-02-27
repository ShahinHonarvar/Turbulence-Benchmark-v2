from itertools import combinations

def if_contains_anagrams(words):

    def sorted_word(word):
        return ''.join(sorted(word.lower()))
    valid_anagrams = 0
    seen = {}
    for word in words:
        sw = sorted_word(word)
        if len(sw) >= 3:
            if sw in seen:
                seen[sw] += 1
                valid_anagrams += seen[sw] - 1
            else:
                seen[sw] = 1
    return valid_anagrams <= 19
from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagrams_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            norm_word = normalize(word)
            anagrams_map[norm_word].append(word)
    anagrams_count = sum((len(anagrams) * (len(anagrams) - 1) // 2 for anagrams in anagrams_map.values()))
    return anagrams_count <= 59
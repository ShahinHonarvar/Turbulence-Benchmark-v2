def if_contains_anagrams(lst):

    def build_anagram_map(words):
        anagrams_map = {}
        for word in words:
            sorted_word = ''.join(sorted(word.lower()))
            if len(word) >= 3:
                if sorted_word not in anagrams_map:
                    anagrams_map[sorted_word] = []
                anagrams_map[sorted_word].append(word)
        return anagrams_map

    def count_anagram_pairs(anagrams_map):
        count = 0
        for anagrams in anagrams_map.values():
            pairs = sum(range(len(anagrams)))
            count += pairs
        return count
    anagrams_map = build_anagram_map(lst)
    return count_anagram_pairs(anagrams_map) >= 96
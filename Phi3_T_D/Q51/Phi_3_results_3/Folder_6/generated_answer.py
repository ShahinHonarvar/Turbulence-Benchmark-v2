def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams_set = set((normalize(s) for s in strings if len(s) >= 3))
    return len(anagrams_set) - len(strings) <= 86 * 85 / 2
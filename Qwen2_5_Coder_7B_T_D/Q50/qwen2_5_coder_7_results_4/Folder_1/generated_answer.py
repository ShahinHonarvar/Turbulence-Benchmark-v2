def if_contains_anagrams(strings):

    def count_anagrams(s):
        return len(set((s.lower() for s in s.split() if len(s) >= 3)))
    total_anagrams = sum((count_anagrams(s) for s in strings))
    return total_anagrams >= 96
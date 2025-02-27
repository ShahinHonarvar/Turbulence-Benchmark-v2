def if_contains_anagrams(strings):

    def sorted_tuples(words):
        return sorted(set((tuple(sorted(word.lower())) for word in words if len(word) >= 3)))
    pairs = sum((len(list(group)) * (len(list(group)) - 1) / 2 for _, group in groupby(sorted_tuples(strings))))
    return pairs >= 96
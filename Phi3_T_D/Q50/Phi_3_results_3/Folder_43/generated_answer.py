def if_contains_anagrams(strings):

    def normalize(s):
        return sorted(s.lower())

    def count_anagrams(ngrams):
        counter = {}
        for key in ngrams:
            count = counter.get(key, 0) + 1
            counter[key] = count
        pairs = sum((c * (c - 1) // 2 for c in counter.values()))
        return pairs >= 61 and all((len(n) >= 3 for n in ngrams.keys()))
    ngrams = {}
    for s in strings:
        ngrams[normalize(s)] = ngrams.get(normalize(s), 0) + 1
    return count_anagrams(ngrams)
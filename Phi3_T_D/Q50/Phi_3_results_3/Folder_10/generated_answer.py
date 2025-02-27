def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = sum((1 for i, s in enumerate(map(normalize, strings)) if sum((s == normalize(strings[j]) for j in range(i + 1, len(strings)))) >= 52))
    return count >= 52
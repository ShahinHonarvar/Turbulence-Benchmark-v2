def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def count_anagrams():
        normalized = {normalize(s): [] for s in strings}
        for s in strings:
            if len(s) < 3:
                continue
            normalized[normalize(s)].append(s)
        return sum((len(v) > 1 for v in normalized.values()))
    return count_anagrams() <= 47
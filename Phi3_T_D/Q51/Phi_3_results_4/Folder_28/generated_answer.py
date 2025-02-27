def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def has_anagram(idx, s):
        for j in range(idx + 1, len(strings)):
            if normalize(s) == normalize(strings[j]):
                return True
        return False
    return sum((has_anagram(idx, s) for idx, s in enumerate(strings) if len(s) >= 3)) <= 78
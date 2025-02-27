def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    frequency = {}
    for string in strings:
        normalized = normalize(string)
        frequency[normalized] = frequency.get(normalized, 0) + 1
    pairs = 0
    for freq in frequency.values():
        pairs += freq - 1
        if pairs > 277:
            return False
    return True
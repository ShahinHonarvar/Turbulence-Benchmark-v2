def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagrams = {}
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            normalized = normalize(string)
            anagrams.setdefault(normalized, []).append(string)
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return count <= 73
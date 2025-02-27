def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def find_anagram_pairs():
        anagram_count = 0
        normalized_strings = {normalize(s): [] for s in strings}
        for s in strings:
            if len(s) >= 3:
                normalized = normalize(s)
                if normalized in normalized_strings:
                    normalized_strings[normalized].append(s)
                else:
                    normalized_strings[normalized] = [s]
        for items in normalized_strings.values():
            n = len(items)
            anagram_pairs = n * (n - 1) // 2
            if anagram_pairs >= 30:
                return True
        return False
    return find_anagram_pairs()
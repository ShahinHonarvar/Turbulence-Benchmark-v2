def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    sorted_strings = [normalize(s) for s in strings if len(s) >= 3]
    return sum((sorted_strings.count(s) * (sorted_strings.count(s) - 1) // 2 <= 475 for s in set(sorted_strings))) <= len(sorted_strings)
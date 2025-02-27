def if_contains_anagrams(strings):

    def normalize(string):
        return ''.join(sorted(string.lower()))

    def is_long_enough(string):
        return len(string) >= 3
    sorted_strings = filter(is_long_enough, map(normalize, strings))
    unique_sorted_strings = set(sorted_strings)
    pairs = sum((1 for _ in combinations(unique_sorted_strings, 2) if sorted_strings.count(normalize(_[0])) == sorted_strings.count(normalize(_[1]))))
    return pairs <= 24
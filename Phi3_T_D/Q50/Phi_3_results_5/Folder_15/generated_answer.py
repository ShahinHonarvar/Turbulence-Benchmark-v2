def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def count_unique_keys(lst):
        return len({normalize(entry) for entry in lst if len(entry) >= 3})
    unique_count = count_unique_keys(strings)
    return unique_count - len(strings) >= 4 * (len(strings) * 2 - unique_count)
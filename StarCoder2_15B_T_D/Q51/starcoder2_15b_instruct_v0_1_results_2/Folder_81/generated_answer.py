def if_contains_anagrams(strings):

    def get_anagrams(strings):
        anagrams = {}
        for string in strings:
            key = ''.join(sorted(string))
            if key in anagrams:
                anagrams[key].append(string)
            else:
                anagrams[key] = [string]
        return [(key, anagrams[key]) for key in anagrams if len(anagrams[key]) > 1]

    def get_english_anagrams(strings):
        letters = set('abcdefghijklmnopqrstuvwxyz')
        return [pair for pair in get_anagrams(strings) if set(pair[0]) == letters]

    def get_long_anagrams(strings):
        return [pair for pair in get_anagrams(strings) if len(pair[0]) >= 3]

    def check_at_most_79_pairs(strings):
        return len(get_long_anagrams(strings)) <= 79

    def check_case_insensitive(strings):
        return len(get_long_anagrams([string.lower() for string in strings])) <= 79
    return check_case_insensitive(strings)
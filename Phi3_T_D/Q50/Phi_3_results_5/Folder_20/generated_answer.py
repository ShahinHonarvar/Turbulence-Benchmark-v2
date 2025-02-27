def if_contains_anagrams(strings):

    def count_char(s):
        return sorted([(ch, s.lower().count(ch)) for ch in set(s.lower()) if ch.isalpha()])
    char_map = {}
    for string in strings:
        if len(string) < 3:
            continue
        char_key = tuple(count_char(string))
        char_map.setdefault(char_key, []).append(string.lower())
    anagram_pairs = 0
    for s in char_map.values():
        anagram_pairs += len(s) * (len(s) - 1) // 2
    return anagram_pairs >= 64
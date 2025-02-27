def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for string in strings:
        if len(string) < 3:
            continue
        norm = normalize(string)
        anagram_count[norm] = anagram_count.get(norm, 0) + 1
    return sum((count * (count - 1) // 2 for count in anagram_count.values())) <= 276
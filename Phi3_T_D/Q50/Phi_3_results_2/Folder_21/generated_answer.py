def if_contains_anagrams(strings_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for string in strings_list:
        if len(string) < 3:
            continue
        norm_str = normalize(string)
        anagram_counts[norm_str] = anagram_counts.get(norm_str, 0) + 1
    return sum((count * (count - 1) // 2 for count in anagram_counts.values())) >= 136
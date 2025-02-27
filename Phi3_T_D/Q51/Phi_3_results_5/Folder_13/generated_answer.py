def if_contains_anagrams(string_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counter = {}
    for s in string_list:
        if len(s) < 3:
            continue
        norm_s = normalize(s)
        counter[norm_s] = counter.get(norm_s, 0) + 1
    anagram_pairs = 0
    for count in counter.values():
        if count >= 2:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 54
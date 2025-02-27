def if_contains_anagrams(strings_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for word in strings_list:
        if len(word) < 3:
            continue
        nw = normalize(word)
        if nw in anagram_count:
            anagram_count[nw] += 1
        else:
            anagram_count[nw] = 1
    return sum((count for count in anagram_count.values() if count > 1)) <= 277
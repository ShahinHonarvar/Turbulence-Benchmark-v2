def if_contains_anagrams(lst):

    def get_key(s):
        return ''.join(sorted(s.lower()))
    anagram_count = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            key = get_key(word)
            if key in anagram_count:
                anagram_count[key] += 1
            else:
                anagram_count[key] = 1
    pairs = 0
    for count in anagram_count.values():
        pairs += count * (count - 1) // 2
    return pairs <= 116
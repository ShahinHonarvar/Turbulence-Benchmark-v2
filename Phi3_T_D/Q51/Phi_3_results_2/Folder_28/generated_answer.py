def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    seen = set()
    for s in lst:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s not in seen:
            seen.add(sorted_s)
            count = sum((is_anagram(s, seen_s) for seen_s in seen))
            anagram_count += count - 1
            seen.add(sorted_s)
    return anagram_count <= 78
def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s.lower()))

    def has_anagram(s, seen):
        sorted_s = sort_string(s)
        if sorted_s in seen:
            return True
        seen.add(sorted_s)
        return False
    seen = set()
    anagram_count = 0
    for s in strings:
        if has_anagram(s, seen):
            anagram_count += 1
    return anagram_count <= 42
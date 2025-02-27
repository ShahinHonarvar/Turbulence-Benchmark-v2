def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = sum((is_anagram(a, b) for a in strings for b in strings if a < b))
    return count <= 289
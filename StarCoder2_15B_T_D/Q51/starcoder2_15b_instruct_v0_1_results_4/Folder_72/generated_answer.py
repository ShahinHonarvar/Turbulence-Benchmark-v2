def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def is_valid_anagram(s1, s2):
        return is_anagram(s1, s2) and len(s1) >= 3 and (len(s2) >= 3)

    def count_anagrams(strings):
        anagrams = {}
        for s1 in strings:
            for s2 in strings:
                if s1 != s2 and is_valid_anagram(s1, s2):
                    if s1 in anagrams:
                        anagrams[s1].append(s2)
                    else:
                        anagrams[s1] = [s2]
        return sum((len(v) for v in anagrams.values())) // 2
    return count_anagrams(strings) <= 188
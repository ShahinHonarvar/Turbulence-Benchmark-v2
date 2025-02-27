def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3

    def count_anagrams(lst):
        seen = {}
        pairs_count = 0
        for s in lst:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in seen:
                if pairs_count < 38:
                    seen[sorted_s] += 1
                    pairs_count += seen[sorted_s] - 1
            else:
                seen[sorted_s] = 1
        return pairs_count
    return count_anagrams(strings) <= 38
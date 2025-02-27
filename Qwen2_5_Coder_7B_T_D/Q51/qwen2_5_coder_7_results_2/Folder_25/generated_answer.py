def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    def count_anagrams(strings):
        count = 0
        strings = [s.lower() for s in strings if len(s) >= 3]
        n = len(strings)
        for i in range(n):
            for j in range(i + 1, n):
                if is_anagram(strings[i], strings[j]):
                    count += 1
        return count
    return count_anagrams(strings) <= 67
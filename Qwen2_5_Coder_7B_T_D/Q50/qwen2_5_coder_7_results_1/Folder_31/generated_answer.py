def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = sum((sum((is_anagram(lst[i], lst[j]) for j in range(i + 1, len(lst)))) for i in range(len(lst))))
    return count >= 68
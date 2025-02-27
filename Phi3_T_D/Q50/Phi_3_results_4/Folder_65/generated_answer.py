def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3
    pairs = [(lst[i], lst[j]) for i in range(len(lst) - 1) for j in range(i + 1, len(lst)) if is_anagram(lst[i], lst[j])]
    return len(pairs) >= 94
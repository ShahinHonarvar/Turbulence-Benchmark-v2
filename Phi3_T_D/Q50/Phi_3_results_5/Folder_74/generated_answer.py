def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def get_anagram_pairs(lst):
        return [(lst[i], lst[j]) for i in range(len(lst)) for j in range(i + 1, len(lst)) if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3]
    return len(get_anagram_pairs(strings)) >= 17
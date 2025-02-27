def if_contains_anagrams(strings):
    """
    Create a function called 'if_contains_anagrams' that takes one argument, a list of strings.
    The function should return true if there are at most 85 pairs of anagrams in the given list;
    otherwise, it should return false. The function should only consider the anagrams of the
    English letters. The function should only consider the anagrams of the length of at least three.
    The function should compare the strings in a case-insensitive manner.
    """

    def is_anagram(s1, s2):
        s1 = ''.join((c for c in s1 if c.isalpha())).lower()
        s2 = ''.join((c for c in s2 if c.isalpha())).lower()
        return sorted(s1) == sorted(s2)
    num_anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                num_anagrams += 1
                if num_anagrams > 85:
                    return False
    return True
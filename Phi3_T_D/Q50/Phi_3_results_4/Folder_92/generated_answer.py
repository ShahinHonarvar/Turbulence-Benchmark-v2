def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    seen_anagrams = set()
    for i, str1 in enumerate(strings):
        for str2 in strings[i + 1:]:
            if is_anagram(str1, str2):
                sorted_anagram = ''.join(sorted(str1.lower()))
                if sorted_anagram not in seen_anagrams:
                    seen_anagrams.add(sorted_anagram)
                    if len(seen_anagrams) >= 2:
                        return True
    return False
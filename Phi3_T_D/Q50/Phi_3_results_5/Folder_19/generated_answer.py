def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    for i, str1 in enumerate(strings):
        for str2 in strings[i + 1:]:
            if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
                anagram_count += 1
                if anagram_count >= 84:
                    return True
    return False
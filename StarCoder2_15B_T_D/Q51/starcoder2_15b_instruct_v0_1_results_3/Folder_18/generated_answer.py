def if_contains_anagrams(list_of_strings):

    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        return sorted(str1) == sorted(str2) and len(str1) >= 3
    anagram_count = 0
    for i in range(len(list_of_strings)):
        for j in range(i + 1, len(list_of_strings)):
            if is_anagram(list_of_strings[i], list_of_strings[j]):
                anagram_count += 1
                if anagram_count > 42:
                    return False
    return anagram_count <= 42
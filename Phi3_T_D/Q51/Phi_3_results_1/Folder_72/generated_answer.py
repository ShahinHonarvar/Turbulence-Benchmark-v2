def if_contains_anagrams(strings_list):

    def is_anagram(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    strings_list = sorted(strings_list, key=str.lower)
    i = 0
    while i < len(strings_list) - 1:
        j = i + 1
        while j < len(strings_list):
            if is_anagram(strings_list[i], strings_list[j]):
                anagram_count += 1
                j += 1
            j += 1
        i += 1
    return anagram_count <= 188
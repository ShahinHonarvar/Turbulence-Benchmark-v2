def if_contains_anagrams(string_list):

    def count_chars(s):
        return sorted(s.lower())
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if count_chars(string_list[i]) == count_chars(string_list[j]):
                anagram_count += 1
                if anagram_count >= 108:
                    return True
    return False
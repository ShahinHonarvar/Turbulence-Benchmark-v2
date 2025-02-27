def if_contains_anagrams(string_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if normalize(string_list[i]) == normalize(string_list[j]):
                    anagram_count += 1
                    if anagram_count >= 8:
                        return True
    return False
def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return all((s1.count(ch) == s2.count(ch) for ch in 'abcdefghijklmnopqrstuvwxyz')) and len(s1) >= 3
    pairs_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]):
                pairs_count += 1
                if pairs_count > 173:
                    return False
    return True
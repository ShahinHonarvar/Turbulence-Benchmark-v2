def if_contains_anagrams(string_list):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3 and are_anagrams(string_list[i], string_list[j]):
                count += 1
    return count >= 86
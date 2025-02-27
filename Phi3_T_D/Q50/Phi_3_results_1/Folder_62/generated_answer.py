def if_contains_anagrams(string_list):

    def count_letters(s):
        return sorted((x for x in s.lower() if x.isalpha()), key=str.lower)
    anagrams_count = 0
    checked_pairs = set()
    for i, s1 in enumerate(string_list):
        for j in range(i + 1, len(string_list)):
            s2 = string_list[j]
            if len(s1) >= 3 and len(s2) >= 3 and ((i, j) not in checked_pairs):
                if count_letters(s1) == count_letters(s2):
                    anagrams_count += 1
                    checked_pairs.add((i, j))
    return anagrams_count >= 43
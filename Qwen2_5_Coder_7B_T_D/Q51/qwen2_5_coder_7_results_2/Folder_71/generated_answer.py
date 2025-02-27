def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    checked_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if (lst[i], lst[j]) not in checked_pairs and (lst[j], lst[i]) not in checked_pairs:
                if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3:
                    anagram_pairs += 1
                    checked_pairs.add((lst[i], lst[j]))
    return anagram_pairs <= 9
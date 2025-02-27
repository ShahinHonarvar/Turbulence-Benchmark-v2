def if_contains_anagrams(strings):

    def count_letters(s):
        return sorted(s.lower())
    anagram_count = 0
    checked_combinations = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            pair = frozenset({i, j})
            if pair not in checked_combinations:
                checked_combinations.add(pair)
                sorted_i, sorted_j = (count_letters(strings[i]), count_letters(strings[j]))
                if sorted_i == sorted_j and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                    anagram_count += 1
    return anagram_count <= 74
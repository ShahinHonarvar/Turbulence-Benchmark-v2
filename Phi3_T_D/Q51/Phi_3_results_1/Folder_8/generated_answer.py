def if_contains_anagrams(strings):

    def strip_non_alpha(s):
        return ''.join(filter(str.isalpha, s)).lower()

    def are_anagrams(str1, str2):
        return sorted(strip_non_alpha(str1)) == sorted(strip_non_alpha(str2))
    count = 0
    checked_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if are_anagrams(strings[i], strings[j]):
                    pair = frozenset({(strings[i], strings[j])})
                    if pair not in checked_pairs:
                        count += 1
                        checked_pairs.add(pair)
    return count <= 68
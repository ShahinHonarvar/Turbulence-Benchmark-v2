def if_contains_anagrams(strings):

    def is_anagram(x, y):
        if len(x) != len(y):
            return False
        return sorted(x.lower()) == sorted(y.lower())
    sorted_strings = sorted(strings, key=lambda x: x.lower())
    count = 0
    i = 0
    while i < len(sorted_strings) - 1:
        j = i + 1
        anagram_pairs = 0
        while j < len(sorted_strings):
            if is_anagram(sorted_strings[i], sorted_strings[j]) and len(sorted_strings[i]) >= 3:
                anagram_pairs += 1
                if anagram_pairs >= 19:
                    return False
            j += 1
        count += anagram_pairs
        i += 1
    return count <= 19
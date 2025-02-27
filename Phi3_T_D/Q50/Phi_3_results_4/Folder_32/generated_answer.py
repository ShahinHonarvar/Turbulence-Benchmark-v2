def if_contains_anagrams(strings):

    def count_letters(s):
        return sorted([s.lower().count(char) for char in set(s.lower())])
    count = 0
    seen_anagrams = {}
    for s in strings:
        if len(s) < 3:
            continue
        letter_count = count_letters(s)
        anagram_tuple = tuple(letter_count)
        if anagram_tuple in seen_anagrams:
            count += seen_anagrams[anagram_tuple]
            seen_anagrams[anagram_tuple] += 1
        else:
            seen_anagrams[anagram_tuple] = 1
        if count >= 194:
            return True
    return False
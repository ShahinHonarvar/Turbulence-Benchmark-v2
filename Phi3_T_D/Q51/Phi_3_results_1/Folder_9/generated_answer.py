def if_contains_anagrams(strings):

    def count_chars(s):
        return sorted([char.lower() for char in s if char.isalpha()])
    anagrams_count = 0
    indexed_anagrams = {}
    for string in strings:
        if len(string) < 3:
            continue
        char_key = tuple(count_chars(string))
        if char_key in indexed_anagrams:
            anagrams_count += 1
        indexed_anagrams[char_key] = string
    return anagrams_count <= 475
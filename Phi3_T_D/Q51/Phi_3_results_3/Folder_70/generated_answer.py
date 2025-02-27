from collections import defaultdict

def if_contains_anagrams(strings):

    def count_letters(s):
        count = defaultdict(int)
        for char in s:
            count[char.lower()] += 1
        return count
    anagrams_count = 0
    string_hashes = {}
    for string in strings:
        string_length = len(string)
        if string_length < 3:
            continue
        letters_count = count_letters(string)
        hash_key = tuple(sorted(letters_count.items()))
        if hash_key in string_hashes:
            anagrams_count += string_hashes[hash_key]
            string_hashes[hash_key] += 1
        else:
            string_hashes[hash_key] = 1
    return anagrams_count <= 97
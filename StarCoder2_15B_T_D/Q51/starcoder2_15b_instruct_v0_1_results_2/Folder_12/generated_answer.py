import hashlib

def if_contains_anagrams(strings):
    anagram_hashes = {}
    num_anagrams = 0
    for string in strings:
        string_hash = hashlib.md5(string.lower().encode()).hexdigest()
        sorted_string = ''.join(sorted(string_hash))
        if sorted_string in anagram_hashes:
            num_anagrams += 1
        else:
            anagram_hashes[sorted_string] = string_hash
        if num_anagrams > 92:
            return False
    return True
def if_contains_anagrams(lst):

    def sort_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    hash_map = {}
    for string in lst:
        if len(string) >= 3:
            sorted_str = sort_string(string)
            if sorted_str in hash_map:
                hash_map[sorted_str].append(string)
            else:
                hash_map[sorted_str] = [string]
    for key, value in hash_map.items():
        if len(value) >= 2:
            anagram_count += len(value) * (len(value) - 1) // 2
    return anagram_count >= 88
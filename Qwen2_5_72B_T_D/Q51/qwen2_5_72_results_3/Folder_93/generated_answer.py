def if_contains_anagrams(arr):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = {}
    for word in arr:
        if len(word) >= 3 and word.isalpha():
            normalized = normalize_string(word)
            if normalized in anagram_dict:
                anagram_count += 1
                if anagram_count > 36:
                    return False
            else:
                anagram_dict[normalized] = True
    return True
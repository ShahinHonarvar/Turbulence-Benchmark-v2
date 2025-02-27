def if_contains_anagrams(strings_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    seen = set()
    for string in strings_list:
        if len(string) < 3:
            continue
        normalized = normalize(string)
        if normalized in seen:
            anagram_count += 1
            if anagram_count > 423:
                return False
        else:
            seen.add(normalized)
    return True
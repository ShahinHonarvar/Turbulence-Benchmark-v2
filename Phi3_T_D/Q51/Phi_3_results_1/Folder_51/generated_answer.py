def if_contains_anagrams(str_list):

    def get_sorted_signature(s):
        return ''.join(sorted(s.lower()))
    seen_signatures = set()
    anagram_pairs = 0
    for word in str_list:
        if len(word) < 3:
            continue
        signature = get_sorted_signature(word)
        if signature in seen_signatures:
            anagram_pairs += 1
        else:
            seen_signatures.add(signature)
        if anagram_pairs > 116:
            return False
    return True
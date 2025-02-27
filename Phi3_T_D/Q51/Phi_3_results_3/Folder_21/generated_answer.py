def if_contains_anagrams(words):

    def get_signature(word):
        return ''.join(sorted(word.lower()))
    signature_count_map = {}
    for word in words:
        if len(word) >= 3:
            signature = get_signature(word)
            if signature in signature_count_map:
                signature_count_map[signature] += 1
            else:
                signature_count_map[signature] = 1
            if signature_count_map[signature] > 1:
                return True
    return False
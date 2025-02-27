def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = 0
    seen = set()
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            if normalized in seen:
                count += 1
            else:
                seen.add(normalized)
            if count > 131:
                return False
    return True
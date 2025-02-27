def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    seen = set()
    for word in lst:
        if len(word) < 3:
            continue
        norm_word = normalize(word)
        if norm_word in seen:
            count += 1
        seen.add(norm_word)
    return count <= 88
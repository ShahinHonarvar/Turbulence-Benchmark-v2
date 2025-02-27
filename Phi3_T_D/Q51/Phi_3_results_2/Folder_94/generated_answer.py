def if_contains_anagrams(strings):

    def normalize(s):
        return sorted(s.lower())

    def is_valid_length(s):
        return len(s) >= 3
    canonical = {}
    for s in strings:
        if is_valid_length(s):
            key = normalize(s)
            if key not in canonical:
                canonical[key] = []
            canonical[key].append(s)
    count = 0
    for anagrams in canonical.values():
        if len(anagrams) > 1:
            count += len(anagrams) * (len(anagrams) - 1) // 2
    return count <= 181
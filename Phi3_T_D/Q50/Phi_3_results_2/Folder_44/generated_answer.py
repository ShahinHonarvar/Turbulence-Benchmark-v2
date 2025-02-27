def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    seen = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            norm_i = normalize(strings[i])
            norm_j = normalize(strings[j])
            if norm_i == norm_j:
                pair = frozenset({strings[i], strings[j]})
                if pair not in seen:
                    count += 1
                    seen.add(pair)
    return count >= 44
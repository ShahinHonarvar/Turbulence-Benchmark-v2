def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def count_anagrams(candidates):
        count = 0
        looks = {}
        for word in candidates:
            if len(word) < 3:
                continue
            key = normalize(word)
            if key in looks:
                count += 1
                looks[key].append(word)
            else:
                looks[key] = [word]
        return count
    unique_keys = set(map(normalize, filter(lambda s: len(s) >= 3, strings)))
    return count_anagrams(unique_keys) >= 155
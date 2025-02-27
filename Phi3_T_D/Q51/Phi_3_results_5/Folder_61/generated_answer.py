def if_contains_anagrams(strings):

    def normalize(s):
        return sorted(s.lower())
    count_dicts = [{} for _ in strings]
    for i, s in enumerate(strings):
        if len(s) > 2:
            word = normalize(s)
            count_dicts[i][word] = count_dicts[i].get(word, 0) + 1
    total_pairs = 0
    for i in range(len(count_dicts)):
        for word, count in count_dicts[i].items():
            if count > 1:
                total_pairs += count * (count - 1) // 2
    return total_pairs <= 50
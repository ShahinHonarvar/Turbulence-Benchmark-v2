def if_contains_anagrams(lst):

    def normalize(s):
        s = s.lower()
        return ''.join(sorted(filter(str.isalpha, s)))
    counts = {}
    for word in lst:
        if len(word) < 3:
            continue
        n_word = normalize(word)
        if n_word in counts:
            counts[n_word] += 1
        else:
            counts[n_word] = 1
    num_pairs = sum((v * (v - 1) // 2 for v in counts.values()))
    return num_pairs <= 74
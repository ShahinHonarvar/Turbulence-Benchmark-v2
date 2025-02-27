def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    normalized_lst = {normalize(s): [] for s in lst if len(s) >= 3}
    for s in lst:
        if len(s) >= 3:
            normalized_word = normalize(s)
            if normalized_word in normalized_lst:
                normalized_lst[normalized_word].append(s)
                count += len(normalized_lst[normalized_word]) - 1
    pairs = count // 2
    return pairs <= 21
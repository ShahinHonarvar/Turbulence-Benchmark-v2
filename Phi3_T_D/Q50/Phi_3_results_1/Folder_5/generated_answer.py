def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    length = len(lst)
    normalized_lst = [(normalize(s), s) for s in lst]
    normalized_set = set(normalized_lst)
    count = 0
    for item in normalized_set:
        index1 = normalized_lst.index(item)
        for item in normalized_lst[index1 + 1:]:
            if item[0] == item[0][::-1]:
                count += 1
                if count >= 20:
                    return True
    return False
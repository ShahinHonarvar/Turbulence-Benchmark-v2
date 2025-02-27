def if_contains_anagrams(strings):
    count = 0
    length_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        length = len(s)
        if length >= 3:
            if sorted_s in length_dict:
                count += length_dict[sorted_s]
                length_dict[sorted_s] += 1
            else:
                length_dict[sorted_s] = 1
    return count >= 20
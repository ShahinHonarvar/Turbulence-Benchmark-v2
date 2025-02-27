def if_contains_anagrams(strings):

    def count_chars(s):
        return ''.join(sorted(s.lower()))
    s_len_3_up = [(count_chars(s), len(s)) for s in strings if len(s) >= 3]
    count = 0
    for i in range(len(s_len_3_up)):
        for j in range(i + 1, len(s_len_3_up)):
            if s_len_3_up[i][0] == s_len_3_up[j][0]:
                count += 1
    return count >= 70
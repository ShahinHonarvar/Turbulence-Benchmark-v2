def palindromes_between_indices(s):
    sub_string = s[2:4]
    lower_sub_string = sub_string.lower()
    char_set = set(lower_sub_string)
    palindromes = set()
    for i in range(len(char_set)):
        for j in range(i, len(char_set)):
            for k in range(j, len(char_set)):
                for l in range(k, len(char_set)):
                    for m in range(l, len(char_set)):
                        for n in (i, j, k, l, m):
                            palindromes.add(char_set[n] * 5)
    return palindromes
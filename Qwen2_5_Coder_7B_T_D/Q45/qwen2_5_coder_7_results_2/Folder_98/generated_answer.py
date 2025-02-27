def palindromes_between_indices(s):
    subset = s[3:6].lower()
    distinct_chars = set(subset)
    palindromes = set()
    for i in range(len(distinct_chars)):
        for j in range(i, len(distinct_chars)):
            for k in range(j, len(distinct_chars)):
                for l in range(k, len(distinct_chars)):
                    char_list = [distinct_chars[i], distinct_chars[j], distinct_chars[k], distinct_chars[l]]
                    if char_list == char_list[::-1]:
                        palindromes.add(''.join(char_list))
    return palindromes
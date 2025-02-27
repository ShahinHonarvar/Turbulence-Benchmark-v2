def palindromes_between_indices(s):
    sub_str = s[4:9]
    sub_str = sub_str.lower()
    unique_chars = set(sub_str)
    palindromes = set()
    for i in range(len(unique_chars)):
        for j in range(i, len(unique_chars)):
            char = unique_chars[i] + unique_chars[j]
            if len(char) >= 3:
                perm = set(itertools.permutations(char))
                for p in perm:
                    p = ''.join(p)
                    if p.lower() == p[::-1].lower() and len(p) >= 6:
                        palindromes.add(p)
    return palindromes
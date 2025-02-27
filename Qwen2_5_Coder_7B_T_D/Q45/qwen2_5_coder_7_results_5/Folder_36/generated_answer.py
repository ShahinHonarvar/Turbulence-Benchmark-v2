def palindromes_between_indices(s):
    subset = s[5:9].lower()
    unique_chars = set(subset)
    if len(unique_chars) < 3:
        return set()
    palindromes = set()
    for i in range(len(unique_chars)):
        for j in range(i, len(unique_chars)):
            for k in range(j, len(unique_chars)):
                for l in range(k, len(unique_chars)):
                    chars = [k for k in unique_chars if k == unique_chars[i] or k == unique_chars[j] or k == unique_chars[k] or (k == unique_chars[l])]
                    for perm in set(permutations(chars)):
                        if len(perm) >= 3 and perm == perm[::-1]:
                            palindromes.add(''.join(perm))
    return palindromes
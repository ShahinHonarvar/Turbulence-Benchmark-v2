def palindromes_between_indices(s):
    extracted_chars = s[6:9]
    unique_chars = set(extracted_chars.lower())
    if len(unique_chars) < 2:
        return set()
    palindromes = set()
    for i in range(len(unique_chars)):
        for j in range(i, len(unique_chars)):
            for k in range(j, len(unique_chars)):
                for l in range(k, len(unique_chars)):
                    for m in range(l, len(unique_chars)):
                        candidate = unique_chars[i] + unique_chars[j] + unique_chars[k] + unique_chars[l] + unique_chars[m]
                        if candidate == candidate[::-1]:
                            palindromes.add(candidate)
    return palindromes
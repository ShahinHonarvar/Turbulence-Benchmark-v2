def palindromes_between_indices(s):
    result = set()
    for i in range(3, 6):
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                for l in range(k + 1, 6):
                    substring = s[i:j + 1] + s[k:l + 1]
                    lower_substring = substring.lower()
                    if lower_substring == lower_substring[::-1] and len(lower_substring) >= 4:
                        result.add(lower_substring)
    return result
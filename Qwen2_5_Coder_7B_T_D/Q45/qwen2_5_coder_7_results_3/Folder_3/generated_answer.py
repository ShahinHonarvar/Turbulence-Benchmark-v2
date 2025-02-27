def palindromes_between_indices(s):
    subset = s[7:10].lower()
    chars = list(subset)
    set_of_palindromes = set()
    for i in range(len(chars)):
        for j in range(i, len(chars)):
            for k in range(j, len(chars)):
                for l in range(k, len(chars)):
                    for m in range(l, len(chars)):
                        substring = chars[i] + chars[j] + chars[k] + chars[l] + chars[m]
                        if substring == substring[::-1] and len(substring) >= 3:
                            set_of_palindromes.add(substring)
    return set_of_palindromes
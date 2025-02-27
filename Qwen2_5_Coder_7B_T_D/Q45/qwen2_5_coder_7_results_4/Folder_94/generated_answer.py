def palindromes_between_indices(s):
    s = s[3:5]
    s = s.lower()
    chars = set(s)
    result = set()
    for i in range(len(chars)):
        for j in range(i, len(chars)):
            for k in range(j, len(chars)):
                for l in range(k, len(chars)):
                    for m in range(l, len(chars)):
                        word = chars[i] * 2 + chars[j] * 2 + chars[k] * 2 + chars[l] * 2 + chars[m] * 2
                        if word == word[::-1] and len(word) >= 3:
                            result.add(word)
    return result
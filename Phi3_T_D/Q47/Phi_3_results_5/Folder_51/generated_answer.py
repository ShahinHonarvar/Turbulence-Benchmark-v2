def palindromes_of_specific_lengths(s):
    s = s[1].lower() + s[2:-1].lower()
    minlen, maxlen = (3, 4)
    n = len(s)
    palindromes = {s[i:j + 1] for i in range(n - minlen + 1) for j in range(i + maxlen - 1, n) if i <= 6 <= j and s[i] == s[j] and all((s[k] in 'abcdefghijklmnopqrstuvwxyz' for k in range(i + 1, j)))}
    return palindromes
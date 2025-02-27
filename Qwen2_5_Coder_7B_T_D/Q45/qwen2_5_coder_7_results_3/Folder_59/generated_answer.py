def palindromes_between_indices(s):
    subset = s[8:10]
    subset = subset.lower()
    chars = sorted(subset)

    def permute(s, l, r):
        if l == r:
            palindromes.add(''.join(s))
        else:
            for i in range(l, r + 1):
                s[l], s[i] = (s[i], s[l])
                permute(s, l + 1, r)
                s[l], s[i] = (s[i], s[l])
    palindromes = set()
    permute(chars, 0, len(chars) - 1)
    return {p for p in palindromes if p == p[::-1] and len(p) >= 3}
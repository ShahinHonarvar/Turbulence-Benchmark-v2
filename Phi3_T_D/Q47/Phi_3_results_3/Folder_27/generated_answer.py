def palindromes_of_specific_lengths(s):

    def to_alpha(c):
        return c.lower() in 'abcdefghijklmnopqrstuvwxyz'
    s = s[13:100]
    palindromes = set()
    for length in range(26, 30):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if all((to_alpha(c) for c in substr)) and substr.lower() == substr[::-1].lower():
                palindromes.add(substr)
    return palindromes
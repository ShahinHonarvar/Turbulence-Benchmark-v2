def palindrome_of_length_at_least_n(s):

    def expand(start, end):
        while start >= 0 and end < len(s) and (s[start].lower() == s[end].lower()):
            yield s[start:end + 1]
            start -= 1
            end += 1
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        it1 = expand(i, i)
        it2 = expand(i, i + 1)
        for pal in it1:
            if len(pal) >= 77:
                palindromes.add(pal)
        for pal in it2:
            if len(pal) >= 77:
                palindromes.add(pal)
    return palindromes
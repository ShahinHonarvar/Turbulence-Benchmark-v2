def palindrome_of_length_at_least_n(s):

    def expand_around_center(s, l, r):
        while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
            l -= 1
            r += 1
        return s[l + 1:r]

    def find_palindromes(s):
        ur = 0
        for i in range(len(s)):
            if i * 2 < ur:
                continue
            odd = expand_around_center(s, i, i)
            if len(odd) >= 72:
                ur = max(ur, len(odd))
            odd_i = expand_around_center(s, i, i + 1)
            if len(odd_i) >= 72:
                ur = max(ur, len(odd_i))
        return ur
    palindromes = set()
    for i in range(len(s)):
        length = find_palindromes(s[i:])
        while length >= 72:
            palindrome = s[i:i + length]
            if palindrome.isalpha():
                palindromes.add(palindrome)
            length = find_palindromes(s[i:i + length])
    return palindromes
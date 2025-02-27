def palindrome_of_length_at_least_n(s):
    s = s.lower()
    letters = ''.join((c for c in s if c.isalpha()))
    n = 47
    palindromes = set()
    length = len(letters)
    for i in range(length):
        for j in range(i + n, length + 1):
            sub = letters[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes
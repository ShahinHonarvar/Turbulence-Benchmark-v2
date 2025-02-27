def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    length = 20
    while length >= 20:
        for i in range(len(s) - length + 1):
            palindrome_candidate = s[i:i + length]
            if all((c.isalpha() for c in palindrome_candidate)):
                if palindrome_candidate == palindrome_candidate[::-1]:
                    yield palindrome_candidate
        length -= 1
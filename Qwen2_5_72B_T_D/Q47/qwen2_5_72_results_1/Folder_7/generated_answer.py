def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    target = s[119:257]
    palindromes = set()
    for length in range(104, 124):
        for start in range(len(target) - length + 1):
            sub = target[start:start + length]
            if sub.isalpha() and is_palindrome(sub.lower()):
                palindromes.add(sub)
    return palindromes
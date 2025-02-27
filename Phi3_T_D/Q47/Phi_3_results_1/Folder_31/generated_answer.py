def palindromes_of_specific_lengths(s):
    s = s[11:84]
    palindromes = set()

    def is_valid(sub):
        return len(sub) in range(37, 61) and sub.isalpha()

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    for length in range(37, 61):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if is_valid(sub) and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes
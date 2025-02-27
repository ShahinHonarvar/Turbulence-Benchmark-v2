def palindrome_of_length_at_least_n(s):

    def is_pali(sub):
        return sub == sub[::-1]
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 90, len(s) + 1):
            if is_pali(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes
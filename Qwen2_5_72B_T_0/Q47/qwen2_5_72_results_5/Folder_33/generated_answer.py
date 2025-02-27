def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[130:296]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 103, min(i + 159, len(s) + 1)):
            if is_palindrome(s[i:j]) and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes
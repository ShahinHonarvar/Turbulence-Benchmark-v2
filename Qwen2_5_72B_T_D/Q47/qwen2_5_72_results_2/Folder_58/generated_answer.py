def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s[125:284]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 109, i + 127):
            if j <= len(s) and is_palindrome(s[i:j].lower()) and s[i:j].isalpha():
                palindromes.add(s[i:j])
    return palindromes
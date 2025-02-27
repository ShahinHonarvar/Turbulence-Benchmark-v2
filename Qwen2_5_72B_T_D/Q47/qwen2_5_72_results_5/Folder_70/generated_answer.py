def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[10:71]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 24, i + 53):
            if j <= len(s):
                potential_palindrome = s[i:j]
                if potential_palindrome.isalpha() and is_palindrome(potential_palindrome):
                    palindromes.add(potential_palindrome)
    return palindromes
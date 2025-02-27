def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    for i in range(10, 60):
        for j in range(i + 18, min(i + 37, 61)):
            substr = s[i:j]
            if is_palindrome(substr) and substr.isalpha():
                result.add(substr)
    return result
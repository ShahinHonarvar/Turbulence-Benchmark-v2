def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s == s[::-1]
    all_palindromes = set()
    for i in range(31):
        for j in range(i + 20, min(i + 31, len(string))):
            substring = string[i:j + 1]
            if is_palindrome(substring) and substring.isalpha():
                all_palindromes.add(substring)
    return all_palindromes
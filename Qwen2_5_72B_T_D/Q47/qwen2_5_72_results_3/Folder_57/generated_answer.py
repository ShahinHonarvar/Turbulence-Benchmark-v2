def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    sub_string = s[16:95]
    palindromes = set()
    for i in range(len(sub_string)):
        for j in range(i + 39, min(i + 53, len(sub_string) + 1)):
            substring = sub_string[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes
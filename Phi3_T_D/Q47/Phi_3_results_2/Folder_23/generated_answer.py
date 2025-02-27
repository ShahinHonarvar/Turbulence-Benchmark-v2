def palindromes_of_specific_lengths(s):

    def is_palindrome_and_valid(sub_str):
        if len(sub_str) < 17 or len(sub_str) > 55:
            return False
        sub_str = sub_str.upper()
        return sub_str == sub_str[::-1] and sub_str.isalpha()
    palindromes = set()
    for i in range(23, 95):
        for j in range(i + 17, min(i + 56, 95 + 1)):
            substring = s[i:j]
            if is_palindrome_and_valid(substring):
                palindromes.add(substring)
    return palindromes
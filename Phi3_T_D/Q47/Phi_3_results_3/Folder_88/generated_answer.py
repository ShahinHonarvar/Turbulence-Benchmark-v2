def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for i in range(11, 88):
        substring = text[i:i + 5]
        if is_palindrome(substring) and substring.isalpha() and (len(substring) in [4, 5]):
            palindromes.add(substring.lower())
        if len(substring) > 1 and is_palindrome(substring[:-1]) and substring[:-1].isalpha() and (len(substring[:-1]) in [4, 5]):
            palindromes.add(substring[:-1].lower())
    return palindromes
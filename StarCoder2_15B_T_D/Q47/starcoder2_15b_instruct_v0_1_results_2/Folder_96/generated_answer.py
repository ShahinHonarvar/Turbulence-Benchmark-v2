def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[100:301]
    for i in range(len(substring) - 50):
        for length in range(50, 101):
            if is_palindrome(substring[i:i + length]):
                palindromes.add(substring[i:i + length].lower())
    return palindromes

def is_palindrome(string):
    return string == string[::-1]
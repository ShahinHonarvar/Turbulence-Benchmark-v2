def palindrome_of_length_n(s):
    palindromes = set()
    shorter_str = s.lower()
    substring_length = 19
    for i in range(len(shorter_str) - substring_length + 1):
        substring = shorter_str[i:i + substring_length]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
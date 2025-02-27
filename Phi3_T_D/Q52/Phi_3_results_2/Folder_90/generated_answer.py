def palindrome_of_length_n(text):
    n = 318
    pivot = n // 2
    string = text.lower()
    palindromes = set()
    for i in range(len(string)):
        if i + n > len(string):
            break
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
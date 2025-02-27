def palindrome_of_length_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 32):
        if string[i:i + 33] == string[i:i + 33][::-1]:
            palindromes.add(string[i:i + 33])
    return palindromes
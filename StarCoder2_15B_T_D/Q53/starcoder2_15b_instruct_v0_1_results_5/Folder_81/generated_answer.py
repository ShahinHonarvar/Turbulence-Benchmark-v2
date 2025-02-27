def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 32):
        for j in range(i + 33, len(string) + 1):
            if string[i:j] == string[i:j][::-1] and string[i:j].isalpha():
                palindromes.add(string[i:j])
    return palindromes
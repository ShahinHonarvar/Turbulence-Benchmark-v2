def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 92):
        for j in range(i + 92, len(string)):
            if string[i:j + 1] == string[i:j + 1][::-1]:
                palindromes.add(string[i:j + 1])
    return palindromes
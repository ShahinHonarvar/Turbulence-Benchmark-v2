def palindrome_of_length_at_least_n(string: str) -> set:
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i:j] == string[i:j][::-1]:
                palindrome = string[i:j].lower()
                if len(palindrome) >= 16 and palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes
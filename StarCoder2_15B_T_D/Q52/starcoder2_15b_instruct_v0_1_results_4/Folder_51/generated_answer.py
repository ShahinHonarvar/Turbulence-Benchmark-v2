def palindrome_of_length_n(string: str) -> set:
    palindromes = set()
    for i in range(len(string) - 72):
        substring = string[i:i + 73]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
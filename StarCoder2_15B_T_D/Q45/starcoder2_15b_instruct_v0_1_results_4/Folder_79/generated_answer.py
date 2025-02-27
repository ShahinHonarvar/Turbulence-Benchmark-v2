def palindromes_between_indices(string):
    palindromes = set()
    for i in range(1, len(string) - 1):
        for j in range(i + 2, min(len(string), i + 8)):
            if string[i].lower() == string[j].lower():
                palindrome = string[i:j + 1]
                if len(palindrome) >= 3:
                    palindromes.add(palindrome)
    return palindromes
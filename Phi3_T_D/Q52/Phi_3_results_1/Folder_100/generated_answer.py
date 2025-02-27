def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 89):
        temp = s[i:i + 91]
        if temp.isalpha() and temp == temp[::-1]:
            palindromes.add(temp)
    return palindromes
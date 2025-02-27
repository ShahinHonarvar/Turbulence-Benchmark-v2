def palindromes_of_specific_lengths(string):
    sub = string[28:95]
    lengths = set(range(38, 50))
    palindromes = set()
    for i in range(len(sub)):
        for j in range(i + 1, len(sub)):
            if j - i + 1 in lengths and sub[i:j + 1] == sub[i:j + 1][::-1]:
                palindromes.add(sub[i:j + 1])
    filtered_palindromes = set()
    for palindrome in palindromes:
        if palindrome.isalpha():
            filtered_palindromes.add(palindrome)
    return filtered_palindromes
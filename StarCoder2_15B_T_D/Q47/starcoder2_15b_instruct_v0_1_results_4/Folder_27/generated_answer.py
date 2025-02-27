def palindromes_of_specific_lengths(string):
    palindromes = set()
    length_range = range(26, 30)
    for length in length_range:
        for i in range(13, 100 - length + 1):
            substring = string[i:i + length]
            is_palindrome = True
            for j in range(length // 2):
                if substring[j].lower() != substring[length - j - 1].lower():
                    is_palindrome = False
                    break
            if is_palindrome:
                palindromes.add(substring)
    return palindromes
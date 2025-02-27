def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    center_start = 18
    center_end = 66
    palindromes = set()
    for center in range(center_start, center_end - 23 + 1):
        for offset in range(1, 9):
            temp = s[center - offset:center + offset + 1].lower()
            if len(temp) >= 23 and len(temp) <= 36 and is_palindrome(temp) and temp.isalpha():
                palindromes.add(temp)
    return palindromes
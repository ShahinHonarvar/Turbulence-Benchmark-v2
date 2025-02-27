def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[26:88].lower()
    for i in range(len(substring)):
        for j in range(i + 52, min(i + 57, len(substring)) + 1):
            palindrome = substring[i:j]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                result.add(palindrome)
    return result
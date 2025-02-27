def palindrome_of_length_n(s):
    s = s.lower()
    two_hundred_twenty_three_palindromes = set()
    for i in range(len(s) - 222):
        substring = s[i:i + 223]
        if substring == substring[::-1]:
            two_hundred_twenty_three_palindromes.add(substring)
    return two_hundred_twenty_three_palindromes
def palindromes_of_specific_lengths(s):
    if len(s) <= 300:
        max_length = len(s)
    else:
        max_length = 300
    start = 0
    palindromes = set()

    def add_palindrome(i, j, current):
        if i - j >= 50 and i - j <= 60:
            palindromes.add(current[j:i])
    while start <= max_length - 50:
        for length in range(50, 61):
            i, j = (start, start + length - 1)
            while i < j and s[i].isalpha() and s[j].isalpha():
                if s[i].lower() == s[j].lower():
                    add_palindrome(i, j, s[start:start + length])
                    break
                i += 1
                j -= 1
        start += 1
    return palindromes
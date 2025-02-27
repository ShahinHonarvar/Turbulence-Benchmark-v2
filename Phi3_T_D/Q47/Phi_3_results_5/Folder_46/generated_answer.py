def expand_around_center(s, l, r):
    count = 0
    while l >= 0 and r < len(s) and (s[l].lower() == s[r].lower()):
        count += 1
        l -= 1
        r += 1
    return count

def palindromes_of_specific_lengths(s):
    lower_bound = 11
    upper_bound = 97
    min_length = 29
    max_length = 62
    palindromes = set()
    for length in range(min_length, max_length + 1):
        for i in range(lower_bound, upper_bound + 1 - length):
            count_odd = expand_around_center(s, i, i + length - 1)
            count_even = expand_around_center(s, i, i + length)
            if count_odd > 0 or count_even > 0:
                palindrome = s[i:i + length]
                if palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes
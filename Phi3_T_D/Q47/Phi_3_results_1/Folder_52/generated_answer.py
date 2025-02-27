def palindromes_of_specific_lengths(s):
    alphanum_s = ''.join([c.lower() for c in s if c.isalpha()])
    palindromes = {alphanum_s[i:j] for i in range(44, 100) for j in range(i + 13, min(i + 43, 100)) if alphanum_s[i:j] == alphanum_s[i:j][::-1]}
    return set((palindrome for palindrome in palindromes if 1 <= len(palindrome) <= 42))
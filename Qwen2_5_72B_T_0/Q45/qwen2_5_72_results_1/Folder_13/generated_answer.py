from collections import Counter

def palindromes_between_indices(s):
    substring = s[3:10].lower()
    letter_counts = Counter(substring)
    odd_chars = [char for char, count in letter_counts.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    half_palindrome = ''.join((char * (count // 2) for char, count in letter_counts.items()))
    palindromes = set()

    def generate_palindromes(half, remaining):
        if not remaining:
            palindrome = half + half[::-1]
            if len(palindrome) >= 5:
                palindromes.add(palindrome)
        else:
            for char in remaining:
                new_half = half + char
                new_remaining = remaining.replace(char, '', 1)
                generate_palindromes(new_half, new_remaining)
    generate_palindromes('', half_palindrome)
    if odd_chars:
        for i in range(len(palindromes)):
            palindrome = list(palindromes)[i]
            middle = len(palindrome) // 2
            new_palindrome = palindrome[:middle] + odd_chars[0] + palindrome[middle:]
            palindromes.add(new_palindrome)
            palindromes.remove(palindrome)
    return palindromes
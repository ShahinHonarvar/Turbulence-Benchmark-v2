from collections import Counter

def palindromes_between_indices(s):
    substring = s[2:6].lower()
    char_count = Counter(substring)
    odd_chars = [char for char, count in char_count.items() if count % 2 != 0]
    if len(odd_chars) > 1:
        return set()
    else:
        even_chars = [char for char, count in char_count.items() if count % 2 == 0]
        half_palindrome = ''.join((char * (char_count[char] // 2) for char in even_chars))
        if odd_chars:
            half_palindrome += odd_chars[0]
        palindromes = set()
        for i in range(len(half_palindrome) + 1):
            for char in even_chars:
                if i == 0:
                    palindromes.add(half_palindrome[:i] + char + half_palindrome[i:])
                else:
                    palindromes.add(half_palindrome[:i] + char + half_palindrome[i:-1])
        return {palindrome for palindrome in palindromes if len(palindrome) >= 3}
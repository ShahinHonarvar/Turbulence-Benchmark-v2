def palindrome_of_length_n(s):
    s = s.lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = {s[i:i + 69] for i in range(len(s) - 68) if set(s[i:i + 69]).issubset(valid_chars)}
    return {p for p in palindromes if p == p[::-1]}
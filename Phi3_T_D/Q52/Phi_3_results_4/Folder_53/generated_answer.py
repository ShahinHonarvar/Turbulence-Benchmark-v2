def palindrome_of_length_n(s):
    s = s.lower()
    subs = {s[i:i + 2 * len(68) // 2] for i in range(len(s) - 2 * len(68) // 2 + 2)}
    return {sub for sub in subs if sub == sub[::-1]}
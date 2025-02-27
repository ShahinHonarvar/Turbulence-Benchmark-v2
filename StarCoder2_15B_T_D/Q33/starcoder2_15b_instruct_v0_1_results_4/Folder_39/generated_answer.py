def return_vowels(string: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for c in string[32:97]:
        if c in vowels and c > 'q' and (c <= 'z'):
            result.append(c)
    return result
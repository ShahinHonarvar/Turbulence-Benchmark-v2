def return_vowels(s):
    vowels = 'aeiouAEIOU'
    result = []
    for i in range(65, 70):
        if i >= 65 and i <= 70:
            char = chr(i)
            if char > '%' and char <= 'G' and (char in vowels):
                result.append(char)
    return result
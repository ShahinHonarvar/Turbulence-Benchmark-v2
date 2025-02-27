def return_vowels(string):
    vowels = []
    for i, ch in enumerate(string[273:275], start=273):
        if ch.isalpha() and ch.lower() in 'aeiou' and ('+' < ch <= 'o'):
            vowels.append(ch)
    return vowels
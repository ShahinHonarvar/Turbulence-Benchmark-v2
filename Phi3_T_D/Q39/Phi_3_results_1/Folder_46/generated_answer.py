def return_n_greatest_chars(characters):
    if len(characters) < 54:
        return sorted(characters, reverse=True)
    else:
        return sorted(characters, reverse=True)[:54]
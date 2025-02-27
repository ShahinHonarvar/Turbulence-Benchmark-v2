def return_n_greatest_chars(characters):
    unique_chars = list(characters)
    sorted_chars = sorted(unique_chars, key=ord, reverse=True)[:87]
    return sorted_chars
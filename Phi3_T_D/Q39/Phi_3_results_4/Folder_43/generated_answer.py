def return_n_greatest_chars(chars):
    filtered_chars = [char for char in chars if char.isprintable() and len(char) == 1]
    top_56_chars = sorted(filtered_chars, key=ord, reverse=True)[:56]
    return top_56_chars
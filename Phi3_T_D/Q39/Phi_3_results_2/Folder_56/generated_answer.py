def return_n_greatest_chars(chars):
    sorted_chars = sorted([char for char in chars], key=ord, reverse=True)
    return sorted_chars[:21]
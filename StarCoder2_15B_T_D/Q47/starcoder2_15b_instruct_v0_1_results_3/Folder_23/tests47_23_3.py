from Q47.starcoder2_15b_instruct_v0_1_results_3.Folder_23.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(94, 55)
    m = min(94 - 23 + 1, 55)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(17, m + 1)}


def test_string_of_similar_nums():
    n = max(94, 55)
    m = min(94 - 23 - 1, 55)
    s = ''.join('0' for _ in range(n * 2))
    assert not palindromes_of_specific_lengths(s)


def test_string_of_distinct_chars():
    s = 'abc' * (94 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_string_of_spaces():
    s = ' ' * (94 * 3)
    assert palindromes_of_specific_lengths(s) == set()


def test_string_of_spaces_and_letters():
    s = ' a ' * (94 * 3)
    assert not palindromes_of_specific_lengths(s)


def test_length_of_palindrome():
    s = ''.join('a' for _ in range(94 * 2))
    returned_result = palindromes_of_specific_lengths(s)
    for i in returned_result:
        assert 17 <= len(i) <= 55


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(94 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[23: 94 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (94 * 3)
    assert not palindromes_of_specific_lengths(s)
    
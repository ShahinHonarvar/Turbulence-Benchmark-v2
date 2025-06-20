from Q47.starcoder2_15b_instruct_v0_1_results_3.Folder_29.generated_answer import palindromes_of_specific_lengths


def test_string_of_similar_chars():
    n = max(94, 73)
    m = min(94 - 15 + 1, 73)
    s = ''.join('a' for _ in range(n * 2))
    assert palindromes_of_specific_lengths(s) == {'a' * i for i in range(18, m + 1)}


def test_string_of_similar_nums():
    n = max(94, 73)
    m = min(94 - 15 - 1, 73)
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
        assert 18 <= len(i) <= 73


def test_location_of_palindrome():
    s = ''.join('a' for _ in range(94 * 3))
    returned_result = palindromes_of_specific_lengths(s)
    sliced_s = s[15: 94 + 1]
    for i in returned_result:
        assert i in sliced_s


def test_string_of_punctuations_and_space():
    s = '@ %' * (94 * 3)
    assert not palindromes_of_specific_lengths(s)
    
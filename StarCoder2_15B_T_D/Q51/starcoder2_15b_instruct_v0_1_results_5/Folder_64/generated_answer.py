def create__code(text_specification: str) -> str:
    """
    Creates  code according to the given text specification. The  code
    should not contain any comments, and should be delimited by triple backticks.
    """
    _code = text_specification.strip('<>').replace('//', '')
    return f
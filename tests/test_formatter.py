from pandoc_run_python.filter import code_formatter



def test_formatter():
    as_is = """
    a = {1:0,
    2:3}
    """

    to_be = """a = {1: 0, 2: 3}
"""

    assert code_formatter(as_is) == to_be

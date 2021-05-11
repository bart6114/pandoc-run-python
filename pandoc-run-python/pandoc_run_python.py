from typing import Callable
import panflute as pf
from panflute import elements

import sys
from io import StringIO

from panflute.base import Element


def py_env_exec() -> Callable:
    d = dict(locals(), **globals())

    def partial_exec(code_text: str) -> str:
        # capture output
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(code_text, d, d)

        # repair default stdout
        sys.stdout = old_stdout
        return redirected_output.getvalue()

    return partial_exec


sprint = lambda x: print(x, file=sys.stderr)
exec_env = py_env_exec()


def action(elem, doc):
    if isinstance(elem, pf.CodeBlock):
        sprint(elem.classes)
        eval_output = exec_env(elem.text)
        return [elem, elements.CodeBlock(eval_output, classes=["python-output"])]


def main(doc=None):
    return pf.run_filter(action, doc=doc)


if __name__ == "__main__":
    main()

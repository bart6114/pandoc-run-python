from typing import Callable
import panflute as pf
from panflute import elements

import io
import sys


def py_env_exec() -> Callable:
    d = dict(locals(), **globals())

    def partial_exec(code_text: str) -> str:
        # capture output
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        exec(code_text, d, d)

        # repair default stdout
        sys.stdout = old_stdout
        return redirected_output.getvalue()

    return partial_exec


def sprint(*args: list, **kwargs: dict) -> None:
    print(*args, **kwargs, file=sys.stderr)


exec_env = py_env_exec()


def action(elem: pf.Element, doc: pf.Doc) -> list:
    # run python code chunks
    if (
        isinstance(elem, pf.CodeBlock)
        and "python" in elem.classes
        and "run" in elem.classes
        and "python-output" not in elem.classes
    ):
        eval_output = exec_env(elem.text)
        return [elem, elements.CodeBlock(eval_output, classes=["python-output"])]
    # remove previously generated output
    elif isinstance(elem, pf.CodeBlock) and "python-output" in elem.classes:
        return []


def remove_elem(elem: pf.Element, doc: pf.Doc) -> pf.Element:
    return elements.Str("")


def main(doc: pf.Doc=None) -> pf.Doc:
    return pf.run_filter(action, doc=doc)


if __name__ == "__main__":
    main()

from typing import Callable
import panflute as pf
from panflute import elements

import io
import sys

from .types import PythonOutput, FigureContainer


def sprint(*args: list, **kwargs: dict) -> None:
    """Print to stderr to avoid showing up as eval ouput."""
    print(*args, **kwargs, file=sys.stderr)


# try to set up custom matplotlib backend
try:
    import matplotlib

    matplotlib.use("module://pandoc_run_python.mpl_backend")

except ImportError:
    sprint("warning: matplotlib not available")


def py_env_exec() -> Callable:
    """Create env to execute code in"""
    d = dict(locals(), **globals())

    def partial_exec(code_text: str) -> PythonOutput:
        po = PythonOutput()
        # capture output
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        code_lines = code_text.splitlines()
        final_line = code_lines[len(code_lines) - 1]

        # hacky tacky
        # first we exec the whole block
        exec("\n".join(code_lines), d, d)

        # then we try to eval last line to see if it returns something
        try:
            res = eval(final_line, d, d)
            if isinstance(res, FigureContainer):
                po.fc = res
            elif res is not None:
                print(res)

        except SyntaxError as err:
            sprint(err)

        # repair default stdout
        sys.stdout = old_stdout
        po.stdout = redirected_output.getvalue()
        return po

    return partial_exec


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
        collector = [elem]
        if eval_output.has_stdout:
            collector.append(
                elements.CodeBlock(eval_output.stdout, classes=["python-output"])
            )
        if eval_output.has_figures:
            for fig in eval_output.fc.figures:
                collector.append(elements.Para(elements.Image(url=str(fig))))

        return collector
    # remove previously generated output
    elif isinstance(elem, pf.CodeBlock) and "python-output" in elem.classes:
        return []


def main(doc: pf.Doc = None) -> pf.Doc:
    return pf.run_filter(action, doc=doc)


if __name__ == "__main__":
    main()

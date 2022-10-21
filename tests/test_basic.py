import panflute as pf
from pathlib import Path
from pandoc_run_python import filter


def doc_loader(fn: str) -> str:
    p = Path(Path(__file__).parent, f"sample_files/{fn}").resolve()
    with open(p) as f:
        doc = pf.convert_text(f.read(), standalone=True)
    return doc


def test_basic():
    doc = doc_loader("simple.md")
    doc_altered = filter.main(doc)
    md_altered = pf.convert_text(
        doc_altered, input_format="panflute", output_format="markdown"
    )
    assert (
        """
``` {.python-output}
Hello World
1
2
3
```"""
        in md_altered
    )


def test_oneline():
    doc = doc_loader("oneline.md")
    doc_altered = filter.main(doc)
    md_altered = pf.convert_text(
        doc_altered, input_format="panflute", output_format="markdown"
    )
    assert (
        """
``` {.python-output}
Hello World
```"""
        in md_altered
    )


def test_wellea():
    doc = doc_loader("simple_wellea.md")
    doc_altered = filter.main(doc)
    md_altered = pf.convert_text(
        doc_altered, input_format="panflute", output_format="markdown"
    )
    assert (
        """``` {.python-output}
4"""
        in md_altered
    )


def test_replace_old_output():
    doc = doc_loader("replace_old.md")
    doc_altered = filter.main(doc)
    md_altered = pf.convert_text(
        doc_altered, input_format="panflute", output_format="markdown"
    )
    assert "``` {.python-output}" in md_altered
    assert "WILL BE REPLACED" not in md_altered


def test_eval_last_value():
    doc = doc_loader("eval_last.md")
    doc_altered = filter.main(doc)
    md_altered = pf.convert_text(
        doc_altered, input_format="panflute", output_format="markdown"
    )
    assert (
        """``` {.python-output}
3
```"""
        in md_altered
    )


def test_eval_no_output():
    doc = doc_loader("no_output.md")
    doc_altered = filter.main(doc)
    md_altered = pf.convert_text(
        doc_altered, input_format="panflute", output_format="markdown"
    )
    assert "python-output" not in md_altered

import panflute as pf
from pathlib import Path
from pandoc_run_python import filter
import io


def doc_loader(fn: str) -> str:
    p = Path(Path(__file__).parent, f"sample_files/{fn}").resolve()
    with open(p) as f:
        doc = pf.convert_text(f.read(), standalone=True)
    return doc


def test_image_insert():
    doc = doc_loader("matplotlib.md")
    doc_altered = filter.main(doc)
    md_altered = pf.convert_text(
        doc_altered, input_format="panflute", output_format="markdown"
    )
    assert "![](figures/" in md_altered

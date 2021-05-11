import panflute as pf
from panflute import elements

import sys

from panflute.base import Element

sprint = lambda x: print(x, file=sys.stderr)

def action(elem, doc):
    if isinstance(elem, pf.CodeBlock):
        sprint(elem.classes)
        sprint(elem.text)
        return [elem, elements.CodeBlock("test\n123", classes=["shell", "python-output"])]


def main(doc=None):
    return pf.run_filter(action, doc=doc) 

if __name__ == '__main__':
    main()

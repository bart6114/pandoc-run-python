import pathlib
import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Header):
        elem.level = 1

def main(doc=None):
    return pf.run_filter(action, doc=doc) 

if __name__ == '__main__':
    main()

# def test_simple_md():
#     assert 3 == 3

def test_print():
    fn = pathlib.Path("./tests/sample_files/1.md")
    with fn.open(encoding='utf-8') as f:
        markdown_text = f.read()

    json_pandoc = pf.convert_text(markdown_text, input_format='markdown', output_format='json', standalone=True)
    print(json_pandoc)
    print(3333)

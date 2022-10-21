[![PyPI](https://img.shields.io/pypi/v/pandoc-run-python)](https://pypi.org/project/pandoc-run-python/)
![CICD](https://github.com/Bart6114/pandoc-run-python/actions/workflows/publish.yml/badge.svg)
[![Downloads](https://pepy.tech/badge/pandoc-run-python)](https://pepy.tech/project/pandoc-run-python)

# pandoc-run-python

This is a [Pandoc filter](https://pandoc.org/filters.html)! 

More specifically it is a filter that allows you to run Python code blocks in your markdown and insert the output of them back into your markdown file. It exists because I enjoy literate programming too much.

It supports capturing the following output of Python code blocks:
- anything printed to `stdout`
- matplotlib-based figures

## Warning 🚨

Make sure that you trust the Python code in your markdown files, they will be executed as-is. A cell with content like `os.system("sudo rm -rf /")` would be painful. In other words, if at any point in the future I send you a markdown file called `money_factory.md` you should NOT run it.

## How to install

```sh
pip install pandoc-run-python
```

## What does it do?


Let's say you have the following markdown file:

````md

## What is fast, loud and crunchy?

```python
print("A rocket chip!")
```

````

When you use this as en example to explain what the output of this `print` statement would be, you'd probably don't want to type the expected output of this command manually. Ideally you want it to be actually evaluated and the output inserted into the markdown file. This way you would automatically end up with something like this:

````md

## What is fast, loud and crunchy?

```python
print("A rocket chip!")
```

```
A rocket chip!
```

````

## pandoc-run-python to the rescue!

Coincidentally, the above is exactly what the `pandoc-run-python` filter provides. How can you achieve this? You need to slightly alter your markdown to specify that a python codeblock needs to be evaluated. More specifically you need to add classes to the codeblock as we did below (I don't like the syntax neither, but this is the pandoc way to do it).


````md

## What is fast, loud and crunchy?

``` {.python .run}
print("A rocket chip!")
```

````

If the previous example would be in a file call `loud.md`, using this pandoc filter you could execute the following command to generate the processed markdown.

```sh
pandoc loud.md -F pandoc-run-python -t markdown
```

````md
## What is fast, loud and crunchy?

``` {.python .run}
print("A rocket chip!")
```

``` {.python-output}
A rocket chip!
```
````

## Auto-formatting

By default, `black` is run on all code chunks denoted with `python` also those that do not have the `run` class.

## Code chunk configuration

This filter runs on all code chunks that has at least the `python` and `run` class.

The following classes are used to determine filter logic:

- `python` and `run`: evaluate code and insert output in a new codeblock / image below the original `python` codeblock
- `no-black`: skip running of the black formatter on python code chunks
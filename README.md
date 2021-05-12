![PyPI](https://img.shields.io/pypi/v/pandoc-run-python)
![CICD](https://github.com/Bart6114/pandoc-run-python/actions/workflows/publish.yml/badge.svg)


# pandoc-run-python

This is a [Pandoc filter](https://pandoc.org/filters.html)! 

More specifically it is a filter that allows you to run Python code blocks in your markdown and insert the output of them back into your markdown file. It exists because I enjoy literate programming too much.

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
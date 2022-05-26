from github_wiki_pydoc import makedoc, page, typedef

from example import example_module
from example.example_module import Primitive, IntArray, ComplexType
from example.example_class import ExampleClass

makedoc(
    pages=(
        page('ExampleClass.md', ExampleClass),
        page('example_module.md', example_module)
    ),
    types=(
        typedef('Primitive', Primitive),
        typedef('IntArray', IntArray),
        typedef('ComplexType', ComplexType)
    ),
    link_root='https://github.com/alcatrazEscapee/github-wiki-pydoc/blob/main',
    content_root='generated',
    home_doc="""
Example description and stuff
""".strip()
)
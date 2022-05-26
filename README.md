# github-wiki-pydoc

A tool to generate a github-wiki for a python library, in a concise, readable form. An alternative to existing tools that are either too complex or rely on external documentation editing and produce subpar results.

### Features

- One page per module or class, with all methods receiving their own line.
- Explicit support for type annotations and type aliases.
- Links to source code (automatic), and relative links (supported via `{@link module#method}` similar to javadoc).
- Interprets `:param:`, `:return:` tags in docstrings correctly.
- Produces markdown formatted specifically for github wiki.
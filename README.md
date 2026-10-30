# Welcome to the VAI Optical Imaging Core Knowledge Base repository

> [!NOTE]
> This is the repository containing the code to the VAI Optical Imaging Core Knowledge
> Base. If you are looking for the website, please go to https://vaioic.github.io.

## Developer's Guide

### Setup

> [!IMPORTANT]
> This project uses [uv](https://docs.astral.sh/uv/) to manage virtual environments and dependencies. 
>
> If you haven't already, you can install ``uv`` by using:
    * **macOS or Linux:** ``curl -LsSf https://astral.sh/uv/install.sh | sh``
    * **Windows:** ``powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"``
>   
> To check if you have ``uv`` installed, open a terminal and run ``uv --version``.

1. Clone the repository:
   ```bash
   git clone git@github.com:vaioic/vaioic.github.io.git
   cd vaioic.github.io
   ```

2. Sync the environment (this will setup the correct virtual environment and dependencies)
   ```bash
   uv sync
   ```

### Authoring the website

1. To maintain consistency, please use [Markdown](https://commonmark.org/help/). You can
   create new pages by adding a ``*.md`` file in the appropriate directory.

3. To build and preview the site, use ``sphinx-autobuild``:
   ```bash
   uv run sphinx-autobuild -b html docs/ docs/_build/html
   ```
   Then open your web browser and navigate to: ``http://localhost:8000``. Changes should
   be reflected automatically.

#### Resources

* [MyST parser](https://myst-parser.readthedocs.io/en/latest/index.html) -
  See the **Authoring** and **Guides** section for more details on the syntax and file
  structure.

## License

This documentation and its associated guides are licensed under the **Creative Commons Attribution 4.0 International License (CC BY 4.0)**. 

See the [LICENSE](LICENSE) file for more details. 

When reusing or adapting these materials, please attribute them to **Van Andel Institute
- Optical Imaging Core**.
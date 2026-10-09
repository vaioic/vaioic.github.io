# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "VAI OIC Knowledge Base"
copyright = "2026, Van Andel Institute Optical Imaging Core"
author = "Van Andel Institute Optical Imaging Core"

version = ""
release = ""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

# File extensions to parse
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# General configuration
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_static_path = ["_static"]
html_css_files = [
    "https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600;700&display=swap",
    "custom.css",
]

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]

html_logo = "_static/logo.png"
html_theme_options = {
    "site_url": "https://vaioic.github.io/",
    "github_url": "https://github.com/vaioic/vaioic.github.io",
    "use_edit_page_button": False,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_start": ["navbar-logo"],
    "show_version_warning_banner": False,
}

html_context = {
    "github_user": "vaioic",
    "github_repo": "vaioic.github.io",
    "github_version": "main",
    "doc_path": "docs",
}

nb_execution_mode = "off"

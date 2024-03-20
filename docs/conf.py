import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Botality'
author = 'UBI-dev'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

language = 'ru'
pygments_style = 'sphinx'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

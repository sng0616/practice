import os
import nbformat
from traitlets.config import Config
from traitlets import  Integer
from nbconvert import HTMLExporter
from nbconvert.preprocessors import Preprocessor
from bs4 import BeautifulSoup


# TIL about os.path.expanduser for relative paths
# ipynb_file = os.path.expanduser('~/Downloads/analysis_responsebias.ipynb')

# Open and read the file as a notebook format
ipynb_file = '/home/snarse/Downloads/analysis_responsebias.ipynb'
ipynb_contents = open(ipynb_file,'r').read()
ipynb_nbformat = nbformat.reads(ipynb_contents, as_version=4)

# print(ipynb_contents)
# Read the notebook content as HTML
html_exporter = HTMLExporter()
html_exporter.template_file = 'basic'
(body, resources) = html_exporter.from_notebook_node(ipynb_nbformat)
# print(body)



# Create a class with a function that reads the entire file by default but only parts when start or end are edited
# class SubCell(Preprocessor):
#     start = Integer(0, help="the first cell of the notebook to be converted")
#     end = Integer(-1, help="the last cell of the notebook to be converted")
#     start.tag(config='True')
#     end.tag(config='True')
#
#     def preprocess(self, nb, resources):
#         self.log.info("Keeping only cells {0} to {1}".format(self.start, self.end))
#         nb.cells = nb.cells[self.start:self.end]
#         return nb, resources
#
# # Create configuration object for SubCell class
# c = Config()
# c.SubCell.start = 7
# c.SubCell.end = 9
# c.HTMLExporter.preprocessors = [SubCell]
#
# # Create the custom exporter
# subcell = HTMLExporter(config=c)
#
# print(subcell.from_notebook_node(ipynb_nbformat)[0])
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# set filepath to notebook for running 
notebook_filename = "./notebooks/analysis_notebook.ipynb"

# set filepath to notebook for output
output_notebook_filename = "./output_notebooks/executed_analysis_notebook.ipynb"

# read in the notebook
with open(notebook_filename) as f_in:
    notebook = nbformat.read(f_in, as_version=4)

# create the ExecutePreprocessor class obbject
notebook_processor = ExecutePreprocessor(timeout=600, kernel_name='python3')

# set the path for the running notebbook.
notebook_processor.preprocess(notebook, {'metadata': {'path': './data/'}})

with open(output_notebook_filename, 'w', encoding='utf-8') as f:
    nbformat.write(notebook, f)
import os
import os.path

from traitlets.config import Config
from nbconvert.exporters.script import ScriptExporter
from nbconvert.exporters.exporter import Exporter

from nbdev.export import *

# class ScalaExporter(ScriptExporter):
class ScalaExporter(ScriptExporter):
    """
    My custom exporter
    """

    # If this custom exporter should add an entry to the
    # "File -> Download as" menu in the notebook, give it a name here in the
    # `export_from_notebook` class member
    export_from_notebook = ".sc (Scala Script)"

    def _file_extension_default(self):
        """
        The new file extension is ``.sc``
        """
        return '.sc'
    
#     def _get_language_exporter(self, lang_name):
#         return '.scala'
    
    def from_notebook_node(self, nb, resources=None, **kw):
        """
        Convert a notebook from a notebook node instance.
        """
#         fname = 
#         for c in nb['cells']:
#             if c["cell_type"] == "code":
                
#         print(nb, type(nb), type(read_nb("test.ipynb")))
        return super().from_notebook_node(nb, resources, **kw)
# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/02_show_scaladoc.ipynb (unless otherwise specified).

__all__ = ['SCRIPT_DIR', 'is_enum', 're_digits_first', 'is_doc_name', 'doc_link']

# Cell
from nbdev.imports import *
from nbconvert import HTMLExporter
from fastcore.utils import IN_NOTEBOOK

if IN_NOTEBOOK:
    from IPython.display import Markdown,display
    from IPython.core import page

# Cell
import sys
import os

SCRIPT_DIR = os.path.dirname(os.getcwd()) + '/chisel_nbdev'
sys.path.append(os.path.normpath(SCRIPT_DIR))
from export_scala import *
from export_scala import get_nbdev_module
from sync_scala import *

# Cell
def is_enum(cls):
    "Check if `cls` is an enum or another type of class"
    return type(cls) in (enum.Enum, enum.EnumMeta)

# Cell
re_digits_first = re.compile('^[0-9]+[a-z]*_')

# Cell
def is_doc_name(name):
    "Test if `name` corresponds to a notebook that could be converted to a doc page"
    for f in Config().path("nbs_path").glob(f'*{name}.ipynb'):
        if re_digits_first.sub('', f.name) == f'{name}.ipynb': return True
    return False

# Cell
def doc_link(name, include_bt=True):
    "Create link to documentation for `name`."
    cname = f'`{name}`' if include_bt else name
    try:
        #Link to modules
        if is_doc_name(name): return f"[{cname}]({Config().doc_baseurl}{name}.html)"
        #Link to local functions
        try_local = source_nb(name, is_name=True)
        print(f'{name} pass try_local')
        if try_local:
            page = re_digits_first.sub('', try_local).replace('.ipynb', '')
            return f'[{cname}]({Config().doc_baseurl}{page}.html#{name})'
        ##Custom links
        mod = get_nbdev_module()
        link = mod.custom_doc_links(name)
        return f'[{cname}]({link})' if link is not None else cname
    except Exception as e: print(e); return cname
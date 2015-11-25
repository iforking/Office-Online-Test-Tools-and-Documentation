# -*- coding: utf-8 -*-
from path import Path


# Load shared config file
execfile(Path('../../_shared/conf.py').abspath())

# -- General configuration -----------------------------------------------------

project = u'Office Online Integration Documentation'

# Configure sphinx.ext.intersphinx
# noinspection PyUnresolvedReferences
intersphinx_mapping = {
    'wopirest':
        ('https://wopi.readthedocs.org/projects/wopirest/en/latest/',
         (
             # Try to load from the locally built docs first
             rest_doc_path / local_object_inventory_path,

             # Fall back to loading from the built docs on readthedocs
             'https://wopirest.readthedocs.org/' + rtd_object_inventory_path
         )),
}

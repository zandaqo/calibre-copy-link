#!/usr/bin/env python

from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'MIT'
__copyright__ = '2020, Maga D. Zandaqo'
__docformat__ = 'restructuredtext en'

from calibre.customize import InterfaceActionBase

class LinksPlugin(InterfaceActionBase):
    name                    = 'Links'
    description             = 'Easily copy and attach links to a selected book'
    supported_platforms     = ['windows', 'osx', 'linux']
    author                  = 'Maga D. Zandaqo'
    version                 = (1, 1, 0)
    minimum_calibre_version = (5, 0, 0)
    actual_plugin           = 'calibre_plugins.links.ui:Links'
        
    def is_customizable(self):
        return False
#!/usr/bin/env python

from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'MIT'
__copyright__ = '2020, Maga D. Zandaqo'
__docformat__ = 'restructuredtext en'

from calibre.customize import InterfaceActionBase

class CopyLinkPlugin(InterfaceActionBase):
    name                    = 'Copy Link'
    description             = 'Easily copy Calibre link to a selected book'
    supported_platforms     = ['windows', 'osx', 'linux']
    author                  = 'Maga D. Zandaqo'
    version                 = (1, 1, 0)
    minimum_calibre_version = (5, 0, 0)
    actual_plugin           = 'calibre_plugins.copy_link.ui:CopyLink'
        
    def is_customizable(self):
        return False
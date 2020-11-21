#!/usr/bin/env python

from PyQt5.Qt import QApplication
from calibre.gui2 import error_dialog
from calibre.ebooks.metadata.book.base import Metadata
from calibre.gui2.actions import InterfaceAction
from calibre.library import current_library_name

class CopyLink(InterfaceAction):
    name = 'Copy Link'
    action_spec = ('Copy Calibre link', None, 'Copy Calibre link to the book', None)
    dont_add_to = frozenset(('context-menu-device',))
    action_type = 'current'
    
    def genesis(self):
        self.qaction.triggered.connect(self.copy_link)        
    
    def copy_link(self):
        id = self._get_selected_ids().pop()
        if id:
            api = self.gui.current_db.new_api
            format = api.formats(id, verify_formats=False)[0]
            link = f'calibre://view-book/{current_library_name()}/{str(id)}/{format}'
            QApplication.clipboard().setText(link)
        
    def _get_selected_ids(self):
        rows = self.gui.library_view.selectionModel().selectedRows()
        if not rows or len(rows) == 0:
            d = error_dialog(self.gui, _('Cannot copy'), _('No books selected'))
            d.exec_()
            return set()
        return set(map(self.gui.library_view.model().id, rows))
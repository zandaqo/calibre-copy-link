#!/usr/bin/env python
import re

from PyQt5.Qt import QApplication, QDesktopServices, QUrl
from calibre.gui2 import error_dialog
from calibre.ebooks.metadata.book.base import Metadata
from calibre.gui2.actions import InterfaceAction

class Links(InterfaceAction):
    name = 'Links'
    action_spec = ('Links', None, None, None)
    dont_add_to = frozenset(('context-menu-device',))
    action_type = 'current'
    action_add_menu = True
    
    def genesis(self):
        self.links_menu = self.qaction.menu()
        self.create_menu_action(self.links_menu, 'copy_link', 'Copy Calibre link', shortcut='Ctrl+L', triggered=self.copy_link)
        self.create_menu_action(self.links_menu, 'open_link', 'Open attached link', shortcut='Ctrl+O', triggered=self.open_link)
        
    def copy_link(self):
        api = self.gui.current_db.new_api
        library_id = getattr(api, 'server_library_id', None)
        if not library_id:
            return
        library_id = '_hex_-' + library_id.encode('utf-8').hex()
        book_id = self.gui.library_view.current_id
        format = api.formats(book_id, verify_formats=False)[0]
        title = api.field_for('title', book_id)
        link = f'[{title}](calibre://view-book/{library_id}/{book_id}/{format})'
        QApplication.clipboard().setText(link)
        
    def open_link(self):
        api = self.gui.current_db.new_api
        book_id = self.gui.library_view.current_id
        link = api.field_for('#attached_link', book_id)
        if not link:
            return
        match = re.match(r'\[.*?\]\((?P<url>.*?)\)', link)
        if match:
            link = match.groupdict()['url']
        url = QUrl(link)
        QDesktopServices.openUrl(url)
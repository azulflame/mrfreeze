"""
Class for coordinating all the different settings modules.

This class loads all of the different settings sub-modules
and provides a single interface for working with them all.
"""

from .server_settings.server_settings import ServerSettings

class Settings:
    def __init__(self):
        self.dbpath = "settings.db"

        # Initialize the sub modules
        self.server_settings = ServerSettings(self.dbpath)

        # Setup tables in the sub modules
        self.server_settings.setup_tables()

        # Expose submodule methods
        self.toggle_freeze_mute = self.server_settings.toggle_freeze_mute
        self.is_freeze_muted    = self.server_settings.is_freeze_muted

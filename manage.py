#!/usr/bin/env python3

"""
CLI to install the backend and manage plugins and data entries
"""

import argparse

from typing import Callable, Sequence


class _Manager:
    """
    Abstract Manager class used to manage resources
    """

    args: argparse.Namespace

    def __init__(self, args):
        """
        Initializes this manager with the argument namespace parsed from the command line by calling parse_args
        """
        self.args = args


def parse_args() -> Callable:
    """
    Parses command line arguments using the argparse module and returns a function to call to
    execute the requested command.
    """
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest="manager")

    subparsers.add_parser("tester", help="testers", description="testers")
    subparsers.add_parser("plugin", help="plugins", description="plugins")
    subparsers.add_parser("data", help="data", description="data")

    for name, parser_ in subparsers.choices.items():
        subsubparser = parser_.add_subparsers(dest="action")

        subsubparser.add_parser("install", help=f"install {parser_.description}")
        subsubparser.add_parser("remove", help=f"remove {parser_.description}")
        subsubparser.add_parser("list", help=f"list {parser_.description}")
        subsubparser.add_parser("clean", help=f"remove {parser_.description} that have been deleted on disk.")

        # TODO: add arguments here to specify which testers/plugins to install/remove and which data entries
        #       to register/unregister

    subparsers.add_parser("install", help="install backend")

    managers = {"install": BackendManager, "tester": TesterManager, "plugin": PluginManager, "data": DataManager}

    args = parser.parse_args()

    if args.manager == "install":
        args.action = "install"

    return getattr(managers[args.manager](args), args.action)


class PluginManager(_Manager):
    """
    Manger for plugins
    """

    def install(self) -> None:
        """
        Install plugins
        """
        # TODO: write code to install a plugin here. This should install the plugin by calling `X.cli install` (where X
        #       is the name of this backend and X.cli is a file in the plugin directory).
        #       This should also update the schema stored in redis as autotest:schema by mergin the plugin schema to
        #       definitions.plugins.properties
        #       Plugin schemas can be retrieved by calling `X.cli settings`.
        #       Store the path to the tester on disk

    def remove(self, additional: Sequence = tuple()):
        """
        Removes installed plugins specified in self.args. Additional plugins to remove can be specified
        with the additional keyword
        """
        # TODO: write code to remove (uninstall) a plugin here.
        #       This should also update the schema stored in redis as autotest:schema by removing the tester schema from
        #       definitions.plugins.properties

    def list(self) -> None:
        """
        Print the name and path of all installed plugins
        """
        # TODO: write code to list (print to stdout) the installed plugins here

    def clean(self) -> None:
        """
        Remove all plugins that are installed but whose data has been removed from disk
        """
        # TODO: write code to remove plugins that have not been cleaned up properly


class TesterManager(_Manager):
    """
    Manager for testers
    """

    def install(self) -> None:
        """
        Install testers
        """
        # TODO: write code to install a tester here. This should install the tester by calling `X.cli install` (where X
        #       is the name of this backend and X.cli is a file in the tester directory).
        #       This should also update the schema stored in redis as autotest:schema by adding the tester name to
        #       definitions.installed_testers.enum and the tester's schema to definitions.tester_schemas.oneOf
        #       Tester schemas can be retrieved by calling `X.cli settings`.
        #       Tester names can be retrieved by inspecting the properties.tester_type.const value in the tester schema.

    def remove(self, additional: Sequence = tuple()) -> None:
        """
        Removes installed testers specified in self.args. Additional testers to remove can be specified
        with the additional keyword
        """
        # TODO: write code to remove (uninstall) a tester here
        #       This should also update the schema stored in redis as autotest:schema by removing the tester name from
        #       definitions.installed_testers.enum and the tester's schema from definitions.tester_schemas.oneOf

    def list(self) -> None:
        """
        Print the name and path of all installed testers
        """
        # TODO: write code to list (print to stdout) the installed testers here

    def clean(self) -> None:
        """
        Remove all testers that are installed but whose data has been removed from disk
        """
        # TODO: write code to remove testers that have not been cleaned up properly


class DataManager(_Manager):
    """
    Manager for data entries.
    Data entries are static files that can be read by the test code run by testers.
    It is highly recommended that all data entries be made read-only by the processes that run each test.
    Otherwise, data may change unexpectedly.
    """

    def install(self) -> None:
        """
        Install a data entry
        """
        # TODO: write code to register a data entry here. Registering involves making the data entry available
        #       to the backend in some way. It does not require creating the data entry itself necessarily.
        #       This should also update the schema stored in redis as autotest:schema by adding the data entry's name
        #       to definitions.data_entries.items.enum

    def remove(self, additional: Sequence = tuple()) -> None:
        """
        Removes installed data entries specified in self.args. Additional entries to remove can be specified
        with the additional keyword
        """
        # TODO: write code to unregister a data entry here. Unregistering involves making the data entry unavailable
        #       to the processes that run tests.
        #       This should also update the schema stored in redis as autotest:schema by removing the data entry's name
        #       from definitions.data_entries.items.enum

    def list(self) -> None:
        """
        Print the name of all installed entries
        """
        # TODO: write code to list (print to stdout) the registered data entries here

    def clean(self) -> None:
        """
        Remove all data entries that are installed but whose data has been removed from disk
        """
        # TODO: write code to unregister data entries that have not been cleaned up properly


class BackendManager(_Manager):
    """
    Manager for the autotest backend
    """

    def install(self) -> None:
        """
        Check that the server is set up properly and create the workspace.
        """
        # TODO: write code to install this backend here. This should write the basic json schema skeleton to the
        #       redis database if it is not already present. The skeleton can be found in `schema_skeleton.json`
        #       and it should be stored in redis as a string at the autotest:schema key.


if __name__ == "__main__":
    parse_args()()

#!/usr/bin/python3
"""console module"""
import cmd
class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quit command to exit console"""
        return True
    def help_quit(self,arg):
        """
        help command 
        """

    def do_EOF(self, arg):
        """EOF command to exit console"""
        return True

    def emptyline(self):
        """doesn't execute anything"""
        pass

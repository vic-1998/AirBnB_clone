#!/usr/bin/python3
"""
Contains the entry point of the command
"""

import cmd
import shlex
import models
from models.base_model import BaseModel


tom = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand(cmd.Cmd):"""
    prompt = '(hbnb)'

    def do_EOF(self, arg):
        """Exit console"""
        return True

    def emptyline(self):
        """shouldnt execute anything"""
        return False

    def do_quit(self, arg):
        """Quit exit de program"""
        return True

    def do_create(self, arg):
        """Create a new instances of the class"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in tom:
            instance = tom[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints string rep. of an instance based"""
        burger = shlex.split(arg)
        if len(burger) == 0:
            print("** class name missing **")
            return False
        if burger[0] in tom:
            if len(burger) > 1:
                beer = burger[0] + "." + burger[1]
                pizza = models.storage.all()
                if beer in pizza:
                    print(pizza[beer])
                else:
                    print("** no instance found **")
                    return False
            else:
                print("** instance id missing **")
                return False
        else:
            print("** class doesn't exist **")
            return False

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in tom:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/env python3
import argparse
from cnt.core import addcontact, listcontacts, deletecontact, search_contact, edit_contact, loadcontacts, save_contact
from cnt.history import show_history

if __name__ == "__main__":
    try:
        parse = argparse.ArgumentParser(
            description="A simple CLI",
            formatter_class=argparse.RawTextHelpFormatter,
            epilog="""\
Usage: cnt <command> [options]

A fast and simple CLI contact manager for your terminal.

CORE COMMANDS:
  add       Add a new contact.
            Required: --name NAME
            Optional: --phone PHONE, --email EMAIL, --tags TAG,...

  list      List all contacts in human-readable format.

  search    Search contacts by filters (all optional, can be combined).
            Options: --id ID, --name NAME, --tag TAG

  delete    Remove a contact by ID.
            Argument: ID

  edit      Modify a single field of an existing contact.
            Required: --id ID, --field FIELD, --value VALUE

  history   Show the change log of all actions (add, edit, delete).

EXAMPLES:
  cnt add --name "John" --phone "+123456789" --email "john@example.com"
  cnt search --name John --tag friend
  cnt edit --id 1 --field phone --value "+987654321"
  cnt delete 1
  cnt history
"""
        )
        
        subparsers = parse.add_subparsers(dest="command")

        parser_add = subparsers.add_parser("add")
        parser_add.add_argument("--name", required=True)
        parser_add.add_argument("--tags", default="")
        parser_add.add_argument("--phone", required=False)
        parser_add.add_argument("--email", required=False)

        subparsers.add_parser("list")

        parser_delete = subparsers.add_parser("delete")
        parser_delete.add_argument("id", type=int)

        parser_search = subparsers.add_parser("search")
        parser_search.add_argument("--id", type=int)
        parser_search.add_argument("--name")
        parser_search.add_argument("--tag")

        parser_edit = subparsers.add_parser("edit")
        parser_edit.add_argument("--id", type=int, required=True)
        parser_edit.add_argument("--field", required=True)
        parser_edit.add_argument("--value", required=True)

        parser_help = subparsers.add_parser("help")
        parser_help.add_argument("topic", nargs="?", default=None)
        
        parser_history = subparsers.add_parser("history")
        
        
        args = parse.parse_args()

        if args.command == "add":
            addcontact(args.name, args.phone, args.email, args.tags)
        elif args.command == "history": 
            show_history()
        elif args.command == "list":
            listcontacts()
        elif args.command == "delete":
            deletecontact(args.id)
        elif args.command == "search":
            search_contact(contact_id=args.id, name=args.name, tag=args.tag)
        elif args.command == "edit":
            edit_contact(args.id, args.field, args.value)
        elif args.command == "help":
            if args.topic and args.topic in subparsers.choices:
                subparsers.choices[args.topic].print_help()
            else:
                parse.print_help()
        else:
            print("cnt: try 'cnt --help' for more information.")
    except SystemExit:
        print("cnt: try 'cnt --help' for more information.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
 

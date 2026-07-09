import json
from json import JSONDecodeError
from .validators import is_phone_valid, is_email_valid, is_duplicate
from .history import logchange, show_history


def loadcontacts():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []

def save_contact(contacts):
    with open("data.json", "w") as f:
        json.dump(contacts, f, indent=4)

def addcontact(name, phone, email, tags):
    contacts = loadcontacts()
    if not name or not name.strip():
        print("Error: Name cannot be empty.")
        return
    if phone:
        if not is_phone_valid(phone):
            print("Please enter a valid phone number.")
            return
    if email:
        if not is_email_valid(email):
            print("Please enter a valid email.")
            return
    if is_duplicate(contacts, phone, email):
        print("A contact with this phone or email already exists.")
        return

    contacts = loadcontacts()
    if not contacts:
        new_id = 1
    else:
        new_id = max(c["id"] for c in contacts) + 1
    if isinstance(tags, str):
        tags_list = [t.strip() for t in tags.split(',') if t.strip()]
    elif isinstance(tags, list):
        tags_list = [t.strip() for t in tags]
    else:
        tags_list = []
    new_contacts = {"id": new_id, "name": name, "phone": phone, "email": email, "tags": tags_list}
    contacts.append(new_contacts)
    save_contact(contacts)
    print(f"Contact {name} added.")
    logchange("ADD", f"Name {name}, ID {new_contacts['id']}")

def deletecontact(contact_id):
    contacts = loadcontacts()
    found = False
    for person in contacts:
        if person["id"] == contact_id:
            found = True
            contacts.remove(person)
            break
    if found == True:
        save_contact(contacts)
        logchange("DELETE", f"ID {contact_id}")
    else:
        print("User does not exist.")
    

def listcontacts():
    data = loadcontacts()
    for person in data:
        print(f"ID: {person['id']}")
        print(f"Name: {person['name']}")
        print(f"Phone: {person['phone']}")
        print(f"Email: {person['email']}")
        tags_str = ', '.join(person['tags']) if person['tags'] else 'None'
        print(f"Tags: {tags_str}")
        print("-" * 30)

def search_contact(contact_id=None, name=None, tag=None):
    data = loadcontacts()
    results = []
    for person in data:
        if contact_id is not None and person["id"] != contact_id:
            continue
        if name is not None and name.lower() not in person["name"].lower():
            continue 
        if tag is not None:
            has_tag = False
            for t in person["tags"]:
                if t.lower() == tag.lower():
                    has_tag = True
                    break
            if not has_tag:
                continue
        results.append(person)

    if not results:
        print("No contacts found.")
    else:
        for person in results:
            print(f"ID: {person['id']}")
            print(f"Name: {person['name']}")
            print(f"Phone: {person['phone']}")
            print(f"Email: {person['email']}")
            tags_str = ', '.join(person['tags']) if person['tags'] else 'None'
            print(f"Tags: {tags_str}")
            print("-" * 30)
        


def edit_contact(contact_id, field, new_value):
    if field != "tags" and (new_value is None or not str(new_value).strip()):
        print("Error: New value cannot be empty.")
        return

    data = loadcontacts()
    found = False
    for person in data:
        if person["id"] == contact_id:
            found = True
            break
    if found == True:
        target_field = field
        person_id = person
        if field == "phone":
            if not is_phone_valid(new_value):
                print("Please enter a valid phone number.")
                return
            if is_duplicate(data, new_value, ""):
                print("Phone number already exists.")
                return
        elif field == "email":
            if not is_email_valid(new_value):
                print("Please enter a valid email.")
                return
            if is_duplicate(data, "", new_value):
                print("Email already exists.")
                return
        if field in ("name", "phone", "email", "tags"):
            if field == "tags":
                if isinstance(new_value, str):
                    tags_list = [t.strip() for t in new_value.split(',') if t.strip()]
                elif isinstance(new_value, list):
                    tags_list = [t.strip() for t in new_value]
                else:
                    tags_list = []
                person_id["tags"] = tags_list
            else:
                person_id[field] = new_value
        else:
            print(f'Invalid field :"{target_field}".')
            return
        save_contact(data)
        logchange("EDIT", f"ID {contact_id}: {field} changed to {new_value}")
        print(f"Contact {contact_id} updated.")
    else:
        print("Contact not found.")

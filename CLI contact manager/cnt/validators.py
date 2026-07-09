import re

def is_phone_valid(contact_phone):
    if not contact_phone: 
        return True
    elif re.fullmatch(r"^\+?\d{7,15}$", contact_phone):
        return True
    else:
        return False
         
def is_email_valid(contact_email):
    if not contact_email:
        return True
    elif re.fullmatch(r"^[^@]+@[^@]+\.[^@]+$", contact_email):
        return True
    else:
        return False

def is_duplicate(contacts,  contact_phone, contact_email):
    if contact_email:
        new_email = contact_email.strip().lower()
    else:
        new_email = ""
    
    if contact_phone:
        new_phone = contact_phone.strip()
    else:
        new_phone = ""

    for person in contacts:
        ext_phone = str(person.get("phone", ""))
        ext_email = str(person.get("email", ""))
        
        ext_phone = ext_phone.strip()
        ext_email = ext_email.strip().lower()
    
        if new_phone != "" and new_phone == ext_phone:
            return True
        
        if new_email != "" and new_email == ext_email:
            return True
        
    return False

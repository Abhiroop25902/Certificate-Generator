from string import Template

def get_contacts(filename: str) -> "tuple[list[str], list[str]]":
    names = []
    emails = []

    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split(',')[0])
            emails.append(a_contact.split(',')[1])

    return names, emails


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def read_credential(filename:str) -> 'list[str]':
    credential  =[]

    with open(filename, mode='r', encoding='utf-8') as stream:
        for line in stream:
            credential.append(line.split()[0])
            credential.append(line.split()[1])

    return credential
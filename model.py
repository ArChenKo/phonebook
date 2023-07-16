from copy import deepcopy

phone_book = {}
path = 'contacts.txt'
original_pb = {}


def next_id():
    if phone_book:
        return max(phone_book)+1
    return 1


def open_f():
    global original_pb
    with open(path, 'r', encoding='utf-8') as file:
        contacts = file.readlines()
    for contact in contacts:
        uid, name, phone, comment = contact.strip().split(';')
        phone_book[int(uid)] = [name, phone, comment]
    original_pb = deepcopy(phone_book)


def save_f():
    with open(path, 'w', encoding='utf-8') as file:
        contacts = []
        for uid, contact in phone_book.items():
            contacts.append(';'.join([str(uid), *contact]))
        contacts = '\n'.join(contacts)
        file.write(contacts)


def add_contact(new: list[str]):
    phone_book[next_id()] = new


def search(find_str: str) -> dict[int, list[str]]:
    result = {}
    for uid, contact in phone_book.items():
        if find_str.lower() in ''.join(contact).lower():
            result[uid] = contact
    return result


def change(uid: int, new: list[str]) -> str:
    contact = phone_book.get(uid)
    for i in range(3):
        if new[i] != '':
            contact[i] = new[i]
    phone_book[int(uid)] = contact
    return contact[0]


def delete(uid: int) -> str:
    return phone_book.pop(uid)[0]

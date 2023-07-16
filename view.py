import text


def print_msg(msg):
    print('\n'+'-'*len(msg))
    print(msg)
    print('-'*len(msg)+'\n')


def show_menu(menu: list[str]) -> int:
    for i, item in enumerate(menu):
        if i != 0:
            print(f'\t{i:>3}. {item}')
        else:
            print(item)
    input_select = input('Выберите пункт меню: ')
    while True:
        if input_select.isdigit() and 0 < int(input_select) < len(menu):
            return int(input_select)
        input_select = input(text.menu_error)


def show_contacts(book: dict[int, list[str]], msg: str):
    max_count = [2, 7, 11]
    if book:
        for contact in book.values():
            for i in range(3):
                if max_count[i] < len(contact[i]):
                    max_count[i] = len(contact[i])
        print('\n'+'-'*(sum(max_count)+13))
        print(
            f'{"ID":>3}.  {"Фамилия Имя":^{max_count[0]}} | '
            f'{"Телефон":^{max_count[1]}} | '
            f'{"Примечание":^{max_count[2]}}')
        print('-' * (sum(max_count) + 13))
        for i, contact in book.items():
            print(
                f'{i:>3}.  {contact[0]:<{max_count[0]}} | '
                f'{contact[1]:<{max_count[1]}} | '
                f'{contact[2]:<{max_count[2]}}')
        print('-' * (sum(max_count) + 13)+'\n')
    else:
        print_msg(msg)


def contact_insert(input_fields: list[str]) -> list[str]:
    contact = []
    for text in input_fields:
        contact.append(input(text))
    return contact


def input_data(msg: str) -> str:
    return input(msg)


def input_num(msg: str) -> int:
    while True:
        num = input(msg)
        if num.isdigit():
            return int(num)
        print(text.num_error)

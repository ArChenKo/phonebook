import view
import text
import model


def search_contacts():
    found_str = view.input_data(text.find_str)
    result = model.search(found_str)
    view.show_contacts(result, text.not_found(found_str))
    return result


def start():
    while True:
        user_select = view.show_menu(text.main_menu)
        match user_select:
            case 1:
                model.open_f()
                view.print_msg(text.load_success)
            case 2:
                model.save_f()
                view.print_msg(text.save_success)
            case 3:
                book = model.phone_book
                view.show_contacts(book, text.empty_book)
            case 4:
                new = view.contact_insert(text.new_contact)
                model.add_contact(new)
                view.print_msg(text.added_success(new[0]))
            case 5:
                search_contacts()
            case 6:
                if search_contacts():
                    uid = view.input_num(text.change_contact)
                    new = view.contact_insert(text.rename_contact)
                    name = model.change(uid, new)
                    view.print_msg(text.renamed_success(name))
            case 7:
                if search_contacts():
                    uid = view.input_num(text.input_del_contact)
                    name = model.delete(uid)
                    view.print_msg(text.delete_success(name))
            case 8:
                if model.phone_book != model.original_pb:
                    if view.input_data(text.save_confirm) == 'да':
                        model.save_f()
                        view.print_msg(text.save_success)
                view.print_msg(text.good_by)
                break

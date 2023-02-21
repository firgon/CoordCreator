from tkinter import filedialog, simpledialog, messagebox


def exit_on_blank(func):
    def fonction(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None or result == '':
            print('vous avez choisi de mettre fin au programme')
            exit()
        else:
            return result

    return fonction


@exit_on_blank
def get_file() -> str:
    return filedialog.askopenfilename()


def get_yes_or_no(ask: str) -> bool:
    return messagebox.askyesno(None, ask)


def get_label(ask) -> str:
    return simpledialog.askstring(None, ask)


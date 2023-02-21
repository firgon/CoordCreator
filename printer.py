


class Printer:

    XY = 'XY'
    RECT = 'rect'
    types = {True: RECT, False: XY}

    def __init__(self, dialog):
        self.dialog = dialog
        self.variable = dialog.get_label(
            "Comment nommer cette variable ?"
        )
        if self.variable == '':
            exit()

        self.type = self.types[
            dialog.get_yes_or_no("Voulez vous enregistrer des rectangles complets ?")
        ]

        self.result = f"{self.variable} = {{ \n"

    def new_record(self, x, y, width, height):
        new_variable = self.dialog.get_label("Quel est le nom de cette valeur ? ")
        if self.type == self.XY:
            self.result += f"   {new_variable} : [{x}, {y}]"
        else:
            self.result += f"   {new_variable} : " \
                           f"[{x:.0f}, {y:.0f}, {width:.0f}, {height:.0f}],\n"

    def finish(self):
        self.result += '}'
        print(self.result)

import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.entry = tk.Entry(root, textvariable=self.result_var, font=('Helvetica', 20), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0

        for text in button_texts:
            tk.Button(self.root, text=text, width=6, height=3, command=lambda t=text: self.on_button_click(t)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button_text):
        current_text = self.result_var.get()

        if button_text == 'C':
            self.result_var.set("0")
        elif button_text == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        else:
            if current_text == '0':
                self.result_var.set(button_text)
            else:
                self.result_var.set(current_text + button_text)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

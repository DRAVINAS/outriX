import tkinter as tk

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.expression = ""
        self.text_input = tk.StringVar()
        self.result_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display current operation - made bigger
        self.entry = tk.Entry(self.root, font=('arial', 28, 'bold'), textvariable=self.text_input, bd=15, insertwidth=4, width=30, borderwidth=5, relief='ridge', justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Label widget to display result - made bigger to match operation box
        self.result_label = tk.Label(self.root, font=('arial', 28, 'bold'), textvariable=self.result_text, bd=15, anchor='e', relief='ridge', bg='white', fg='blue')
        self.result_label.grid(row=1, column=0, columnspan=4, sticky="nsew")

        # Button layout
        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
            ('0', 5, 0), ('C', 5, 1), ('=', 5, 2), ('/', 5, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=20, font=('arial', 18, 'bold'),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")

        # Configure grid weights for resizing
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.text_input.set("")
            self.result_text.set("")
        elif char == '=':
            try:
                result = str(eval(self.expression))
                self.result_text.set(result)
            except Exception:
                self.result_text.set("Error")
            # Keep the expression visible in the entry
        else:
            self.expression += str(char)
            self.text_input.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()

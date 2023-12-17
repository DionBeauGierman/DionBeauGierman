import tkinter as tk

def calculate_fibonacci():
    length = int(entry.get())
    a, b = 0, 1
    sequence = [a, b]
    for _ in range(2, length):
        a, b = b, a + b
        sequence.append(b)
    result_label.config(text=f"The Fibi sequence with length {length} is: {sequence}")

window = tk.Tk()
window.title("fibi calc")

input_label = tk.Label(window, text="Enter sequence length:")
input_label.grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(window)
entry.grid(row=0, column=1, padx=10, pady=10)

calculate_button = tk.Button(window, text="Calculate", command=calculate_fibonacci)
calculate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(window, text="", wraplength=300)
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
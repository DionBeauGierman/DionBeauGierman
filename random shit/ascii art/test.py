from tkinter import filedialog as fd

file_path = fd.askopenfilename()

print(file_path.split('.')[-1:], file_path)
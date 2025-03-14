import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from intelhex import IntelHex

class HexToBinConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("HEX to BIN Converter")
        self.root.geometry("600x400")

        # Load Button
        self.load_button = tk.Button(root, text="Load HEX File", command=self.load_hex_file)
        self.load_button.pack(pady=10)

        # Hex Dump Display
        self.hex_display = scrolledtext.ScrolledText(root, width=70, height=15, wrap=tk.WORD)
        self.hex_display.pack(pady=10)

        # Convert & Save Button
        self.convert_button = tk.Button(root, text="Convert to BIN & Save", command=self.convert_to_bin)
        self.convert_button.pack(pady=10)

        self.hex_file_path = None

    def load_hex_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Intel HEX files", "*.hex")])
        if file_path:
            self.hex_file_path = file_path
            self.display_hex_dump(file_path)

    def display_hex_dump(self, file_path):
        try:
            with open(file_path, "r") as hex_file:
                hex_content = hex_file.readlines()
            
            self.hex_display.delete("1.0", tk.END)
            for line in hex_content:
                self.hex_display.insert(tk.END, line)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to read HEX file:\n{e}")

    def convert_to_bin(self):
        if not self.hex_file_path:
            messagebox.showwarning("Warning", "No HEX file loaded!")
            return

        try:
            ih = IntelHex(self.hex_file_path)
            bin_file_path = os.path.splitext(self.hex_file_path)[0] + ".bin"
            ih.tofile(bin_file_path, format="bin")
            messagebox.showinfo("Success", f"BIN file saved:\n{bin_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HexToBinConverter(root)
    root.mainloop()

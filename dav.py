import os
import subprocess
import sys

# Full Tkinter GUI code to write into cal.py
gui_code = """import tkinter as tk
from tkinter import messagebox
from decimal import Decimal, InvalidOperation

class SafeAdderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Adder App")
        self.root.geometry("300x200")
        
        tk.Label(root, text="Enter First Number:").pack(pady=2)
        self.entry1 = tk.Entry(root)
        self.entry1.pack(pady=2)
        
        tk.Label(root, text="Enter Second Number:").pack(pady=2)
        self.entry2 = tk.Entry(root)
        self.entry2.pack(pady=2)
        
        tk.Button(root, text="Add Numbers", command=self.calculate_sum).pack(pady=10)
        
        self.label_result = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
        self.label_result.pack(pady=5)

    def calculate_sum(self):
        val1 = self.entry1.get().strip()
        val2 = self.entry2.get().strip()
        if not val1 or not val2:
            messagebox.showwarning("Missing Data", "Both input fields must be filled.")
            return
        try:
            n1 = Decimal(val1)
            n2 = Decimal(val2)
            self.label_result.config(text=f"Result: {n1 + n2}", fg="green")
        except InvalidOperation:
            messagebox.showerror("Invalid Input", "Please enter valid numeric characters only.")
            self.label_result.config(text="Result: Error", fg="red")

if __name__ == '__main__':
    root = tk.Tk()
    app = SafeAdderApp(root)
    root.mainloop()
"""

try:
    # 1. Target the Desktop directory automatically
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop, "cal.py")

    # 2. Write the file safely to your desktop
    print(f"[*] Creating file at: {file_path}")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(gui_code)
    print("[+] cal.py created successfully on your Desktop!")

    # 3. Change directory to Desktop and trigger PyInstaller automatically
    print("[*] Running PyInstaller package builder, please wait...")
    os.chdir(desktop)

    # Use the current Python environment's version of PyInstaller
    result = subprocess.run(
        [sys.executable, "-m", "PyInstaller", "--noconsole", "--onefile", "cal.py"],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        print("\n" + "=" * 40)
        print("[SUCCESS] App compiled successfully!")
        print(f"[+] Look on your Desktop for a folder called 'dist'.")
        print("[+] Inside the 'dist' folder is your standalone downloadable app file!")
        print("=" * 40)
    else:
        print("\n[!] PyInstaller encountered an error:")
        print(result.stderr)
        print("\n[*] Attempting to install pyinstaller for you just in case...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("[*] Please run this script one more time now that PyInstaller is ready.")

except Exception as e:
    print(f"[!] An unexpected error occurred: {e}")

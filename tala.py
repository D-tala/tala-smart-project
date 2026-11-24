import tkinter as tk
from tkinter import messagebox
from decimal import Decimal, InvalidOperation # Fixes decimal precision issues

class SafeAdderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Production-Ready Adder")
        self.root.geometry("300x200")
        
        # Build UI Components safely inside a class structure
        tk.Label(root, text="Enter a Number:").pack(pady=2)
        self.entry1 = tk.Entry(root)
        self.entry1.pack(pady=2)
        
        tk.Label(root, text="Enter Another Number:").pack(pady=2)
        self.entry2 = tk.Entry(root)
        self.entry2.pack(pady=2)
        
        tk.Button(root, text="Add Numbers", command=self.calculate_sum).pack(pady=10)
        
        self.label_result = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
        self.label_result.pack(pady=5)

    def calculate_sum(self):
        val1 = self.entry1.get().strip()
        val2 = self.entry2.get().strip()
        
        # Specific UX check for empty inputs
        if not val1 or not val2:
            messagebox.showwarning("Missing Data", "Both input fields must be filled.")
            return

        try:
            # Using Decimal instead of Float prevents precision math errors (e.g., 0.1 + 0.2 = 0.3)
            n1 = Decimal(val1)
            n2 = Decimal(val2)
            
            result = n1 + n2
            self.label_result.config(text=f"Result: {result}", fg="green")
            
        except InvalidOperation:
            messagebox.showerror("Invalid Input", "Please enter valid numeric characters only.")
            self.label_result.config(text="Result: Error", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = SafeAdderApp(root)
    root.mainloop()

import subprocess
import tkinter as tk
from tkinter import filedialog


def convert_readme_to_pdf():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show a file dialog to choose the input file
    readme_file_path = filedialog.askopenfilename(
        title="Select README file",
        filetypes=(("Markdown files", "*.md"), ("All files", "*.*")),
    )

    # Show a file dialog to choose the output file
    pdf_file_path = filedialog.asksaveasfilename(
        title="Save PDF as",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")),
        defaultextension=".pdf",
    )

    command = f"mdpdf {readme_file_path} -o {pdf_file_path}"
    process = subprocess.Popen(command, shell=True)
    process.wait()


# Usage:
convert_readme_to_pdf()

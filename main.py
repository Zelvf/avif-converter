import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from PIL import Image
import pillow_avif  # Registers AVIF support

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class AvifConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("JPG/PNG to AVIF Converter")
        self.geometry("600x500")

        self.selected_files = []
        self.output_dir = ""

        # UI Elements
        self.label = ctk.CTkLabel(self, text="Select JPG or PNG files to convert", font=("Arial", 16))
        self.label.pack(pady=10)

        self.select_button = ctk.CTkButton(self, text="Select Files", command=self.select_files)
        self.select_button.pack(pady=5)

        self.files_label = ctk.CTkLabel(self, text="No files selected", wraplength=500)
        self.files_label.pack(pady=5)

        # Output Directory Selection
        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.pack(pady=10, fill="x", padx=40)

        self.output_button = ctk.CTkButton(self.output_frame, text="Select Output Folder", command=self.select_output_dir, fg_color="gray")
        self.output_button.pack(side="left", padx=10, pady=10)

        self.output_label = ctk.CTkLabel(self.output_frame, text="Default: Same as source", wraplength=300)
        self.output_label.pack(side="right", fill="x", expand=True, padx=10)

        self.quality_frame = ctk.CTkFrame(self)
        self.quality_frame.pack(pady=10, fill="x", padx=40)

        self.quality_label = ctk.CTkLabel(self.quality_frame, text="Quality: 80")
        self.quality_label.pack(side="left", padx=10)

        self.quality_slider = ctk.CTkSlider(self.quality_frame, from_=1, to=100, number_of_steps=100, command=self.update_quality_label)
        self.quality_slider.set(80)
        self.quality_slider.pack(side="right", fill="x", expand=True, padx=10)

        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=20, fill="x", padx=40)

        self.convert_button = ctk.CTkButton(self, text="Convert to AVIF", command=self.start_conversion, state="disabled")
        self.convert_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=5)

    def update_quality_label(self, value):
        self.quality_label.configure(text=f"Quality: {int(value)}")

    def select_files(self):
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        if files:
            self.selected_files = list(files)
            file_count = len(self.selected_files)
            self.files_label.configure(text=f"{file_count} files selected")
            self.convert_button.configure(state="normal")
            self.progress_bar.set(0)
            self.status_label.configure(text="")

    def select_output_dir(self):
        directory = filedialog.askdirectory(title="Select Output Directory")
        if directory:
            self.output_dir = directory
            self.output_label.configure(text=f"Save to: {os.path.basename(directory)}")

    def start_conversion(self):
        if not self.selected_files:
            return

        self.convert_button.configure(state="disabled")
        self.select_button.configure(state="disabled")
        self.output_button.configure(state="disabled")
        self.quality_slider.configure(state="disabled")
        
        # Run conversion in a separate thread to keep GUI responsive
        thread = threading.Thread(target=self.convert_files)
        thread.start()

    def convert_files(self):
        quality = int(self.quality_slider.get())
        total = len(self.selected_files)
        
        for i, file_path in enumerate(self.selected_files):
            try:
                self.status_label.configure(text=f"Converting: {os.path.basename(file_path)}...")
                img = Image.open(file_path)
                
                # Create output filename
                file_name = os.path.basename(file_path)
                base_name = os.path.splitext(file_name)[0]
                
                if self.output_dir:
                    output_path = os.path.join(self.output_dir, f"{base_name}.avif")
                else:
                    output_path = os.path.join(os.path.dirname(file_path), f"{base_name}.avif")
                
                # Save as AVIF
                img.save(output_path, "AVIF", quality=quality)
                
                # Update progress
                progress = (i + 1) / total
                self.progress_bar.set(progress)
                
            except Exception as e:
                print(f"Error converting {file_path}: {e}")
                self.after(0, lambda: messagebox.showerror("Error", f"Failed to convert {os.path.basename(file_path)}: {e}"))
                break

        self.after(0, self.finish_conversion)

    def finish_conversion(self):
        self.status_label.configure(text="Conversion complete!")
        self.convert_button.configure(state="normal")
        self.select_button.configure(state="normal")
        self.output_button.configure(state="normal")
        self.quality_slider.configure(state="normal")
        messagebox.showinfo("Success", "All files converted successfully!")

if __name__ == "__main__":
    app = AvifConverterApp()
    app.mainloop()

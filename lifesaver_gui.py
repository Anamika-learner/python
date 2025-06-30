import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib import pyplot as plt

def select_and_detect():
    # OLD image
    old_path = filedialog.askopenfilename(title="Select OLD Satellite Image")
    if not old_path:
        return

    # NEW image
    new_path = filedialog.askopenfilename(title="Select NEW Satellite Image")
    if not new_path:
        return

    old = cv2.imread(old_path, cv2.IMREAD_GRAYSCALE)
    new = cv2.imread(new_path, cv2.IMREAD_GRAYSCALE)

    if old is None or new is None:
        messagebox.showerror("Error", "Image not found or cannot be opened.")
        return

    # Resize images to same shape
    new = cv2.resize(new, (old.shape[1], old.shape[0]))

    # Absolute difference
    diff = cv2.absdiff(old, new)

    # Thresholding
    _, change = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # % change
    change_percent = (np.count_nonzero(change) / change.size) * 100

    # Alert
    alert = "🚨 Major Change Detected!" if change_percent > 10 else "✔ Minor Change Only"

    # Show in Matplotlib
    plt.figure(figsize=(10, 4))
    plt.suptitle(f"{alert} | Change: {change_percent:.2f}%", fontsize=14)

    plt.subplot(1, 3, 1)
    plt.imshow(old, cmap='gray')
    plt.title("Old Image")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(new, cmap='gray')
    plt.title("New Image")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(change, cmap='gray')
    plt.title("Detected Change")
    plt.axis('off')

    plt.tight_layout()
    plt.show()

# GUI window
window = tk.Tk()
window.title("Life Saver System - Satellite Change Detector")
window.geometry("400x200")
window.configure(bg="#e1f5fe")

tk.Label(window, text="🛰 Life Saver System", font=("Arial", 16, "bold"), bg="#e1f5fe").pack(pady=10)
tk.Button(window, text="🖼️ Select Images & Detect Change", font=("Arial", 12), command=select_and_detect).pack(pady=20)
tk.Label(window, text="Made by Anamika", font=("Arial", 10), bg="#e1f5fe").pack(side="bottom", pady=10)

window.mainloop()

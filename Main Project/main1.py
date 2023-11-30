import tkinter as tk

def change_image():
    # Load a new image
    new_image = tk.PhotoImage(file="2.png")
    
    # Update the label with the new image
    label.config(image=new_image)
    label.image = new_image  # Keep a reference to prevent garbage collection

root = tk.Tk()
root.title("Image Changer")

# Load the initial image
initial_image = tk.PhotoImage(file="1.png")

# Create a label to display the image
label = tk.Label(root, image=initial_image)
label.pack()

# Create a button to change the image
change_button = tk.Button(root, text="Change Image", command=change_image)
change_button.place(y = 500, x = 280)

root.mainloop()

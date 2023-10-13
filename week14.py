import tkinter as tk

class LEDSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Simulator")
        
        self.led_on = False
        self.led_label = tk.Label(root, text="LED OFF", font=("Arial", 20))
        self.led_label.pack(pady=20)
        
        self.toggle_button = tk.Button(root, text="Toggle LED", command=self.toggle_led)
        self.toggle_button.pack()
    
    def toggle_led(self):
        self.led_on = not self.led_on
        if self.led_on:
            self.led_label.config(text="LED ON", fg="green")
        else:
            self.led_label.config(text="LED OFF", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = LEDSimulator(root)
    root.mainloop()

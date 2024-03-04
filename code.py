import tkinter as tk
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog
import pyshark
import os

class PacketSniffer:
   def __init__(self, interface):

       self.interface = interface
       self.packet_data = ""

   def start_sniffing(self):

       # Specify the path of the TShark executable
       capture = pyshark.LiveCapture(interface=self.interface, tshark_path="C:/Program Files/Wireshark/tshark.exe")

       # Start capturing packets
       capture.sniff(packet_count=50, timeout=30)

       for packet in capture:
           self.packet_data += str(packet) + "\n"
           self.display_packet(str(packet))

   def display_packet(self, packet_data):

       # Display the captured packet in the text area
       text_area.insert(tk.END, packet_data + "\n")
       text_area.tag_configure("packet", foreground="white", background="black")  # Customize the packet styling here

def start_sniffer():

   # Get the interface entered by the user
   interface = interface_entry.get()
   sniffer = PacketSniffer(interface)
   sniffer.start_sniffing()

def save_packets():
   # Open a file dialog to choose the save location
   file_path = filedialog.asksaveasfilename(defaultextension=".txt")

   if file_path:
       # Check if the file exists
       if not os.path.exists(file_path):
           # Create the file if it doesn't exist
           with open(file_path, "w") as file:
               pass

       # Save the captured packets to the chosen file
       with open(file_path, "a") as file:
           file.write(sniffer.packet_data)

def clear_packets():
   # Clear the text area
   text_area.delete("1.0", tk.END)

# Create the root window
root = tk.Tk()
root.title("Packet Sniffer")

# Customize the interface styling here
root.configure(background="red")  # Set the background color of the root window

# Create a label for the interface
interface_label = tk.Label(root, text="Interface:", fg="black", bg="yellow")  # Set the label foreground and background colors
interface_label.pack()

# Create an entry for the interface
interface_entry = tk.Entry(root, bg="white")  # Set the entry background color
interface_entry.pack()

# Create a button to start the sniffer
start_button = tk.Button(root, text="Start Sniffing", command=start_sniffer, bg="yellow", fg="black")  # Set the button colors
start_button.pack()

# Create a button to save captured packets
save_button = tk.Button(root, text="Save Packets", command=save_packets, bg="blue", fg="white")  # Set the button colors
save_button.pack()

# Create a button to clear the displayed packets
clear_button = tk.Button(root, text="Clear Packets", command=clear_packets, bg="green", fg="white")  # Set the button colors
clear_button.pack()

# Create a text area to display the captured packets
text_area = scrolledtext.ScrolledText(root, bg="black", fg="white")  # Set the text area foreground and background colors

text_area.pack()

# Run the main event loop
root.mainloop()

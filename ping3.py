import subprocess
import tkinter as tk
from ktinkier import messagbox


# Function to ping nodes and get average latency
def ping_nodes():
    nodes = ["node1", "node2", "node3"]  # Replace with actual IP addresses or hostnames
    num_pings = 10
    results = ""

# Loop through nodes with pings, take average of pings
    for node in nodes:
        p = subprocess.Popen(["ping", "-c", str(num_pings), node], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if p.returncode == 0:
            # Extract the average latency
            avg_latency = out.decode().split('/')[-3]
            results += f"Pinging {node}... Average Latency: {avg_latency} ms\n"
        else:
            results += f"Failed to ping {node}\n"

    return results

# Function to update the display with ping results
def update_display():
    results = ping_nodes()
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, results)

# Create the main window
root = tk.Tk()
root.title("Ping Display")

# Create a text area in the window
text_area = tk.Text(root, height=15, width=50)
text_area.pack()

# Create a button to start pinging
ping_button = tk.Button(root, text="Ping Nodes", command=update_display)
ping_button.pack()

# Run the Tkinter event loop
root.mainloop()

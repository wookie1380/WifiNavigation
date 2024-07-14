import subprocess
import tkinter as tk


# Function to ping nodes and get average latency
def ping_nodes():
    nodes = ["192.168.1.105", "192.168.1.145", "192.168.1.1"]  # Replace with actual IP addresses or hostnames
    num_pings = 10
    results = ""

    for node in nodes:
        # Run the ping command with subprocess
        process = subprocess.Popen(["ping", "-n", str(num_pings), node], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        out = out.decode('utf-8')

        # Check if ping was successful
        if process.returncode == 0:
            # Extract the average latency
            avg_latency = out.split('Average = ')[1].split('ms')[0]
            results += f"Pinging {node}... Average Latency: {avg_latency} ms\n"
        else:
            results += f"Failed to ping {node}\n"

    return results


# Function to update the display with ping results
def update_display():
    results = ping_nodes()
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, results)


# Create cartesian plane
root = tk.Tk()

canvas = tk.Canvas(root, height=400, width=400)
canvas.create_window(200, 200)
canvas.create_line(0, 200, 399, 200, dash=(2, 2))  # x-axis
canvas.create_line(200, 0, 399, 200, dash=(2, 2))  # x-axis


# Add node points

# Add variable node to be tracked


# If everything is working, add and remove nodes

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

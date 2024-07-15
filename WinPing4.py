import subprocess
import threading
import tkinter as tk


def ping_node(node, num_pings):
    results = []

    # Run the ping command
    process = subprocess.Popen(["ping", "-n", str(num_pings), node], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode('utf-8')

    # Check if ping was successful
    if process.returncode == 0:
        # Extract individual pings and average latency
        lines = out.splitlines()
        for line in lines:
            if 'time=' in line:
                latency = line.split('time=')[1].split(' ')[0]
                results.append(latency)
        avg_latency = out.split('Average = ')[1].split('ms')[0]
        results.append(f"Average Latency: {avg_latency} ms")
    else:
        results.append(f"Failed to ping {node}")

    return results


def ping_multiple_nodes(nodes, num_pings):
    threads = []
    results = {}

    for node in nodes:
        thread = threading.Thread(target=lambda n=node: results.update({n: ping_node(n, num_pings)}))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results


def update_gui(results):
    root = tk.Tk()
    root.title("Ping Results")

    for node, result in results.items():
        label_node = tk.Label(root, text=f"Pinging {node}:")
        label_node.pack()

        for line in result:
            label_result = tk.Label(root, text=line)
            label_result.pack()

        separator = tk.Frame(root, height=2, bd=1, relief=tk.SUNKEN)
        separator.pack(fill=tk.X, padx=5, pady=5)

    root.mainloop()


# Example usage
if __name__ == "__main__":
    nodes = ["192.168.0.10", "127.0.0.1", "192.168.0.1", "example.com"]  # Replace with your nodes
    num_pings = 5

    results = ping_multiple_nodes(nodes, num_pings)
    update_gui(results)

# Add validation to user input for node ip addresses, using regex

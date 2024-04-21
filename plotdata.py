import json
import matplotlib.pyplot as plt

# Load the JSON data
with open('stockdata.json') as f:
    data = json.load(f)

# Extracting relevant data
symbols = [entry['Symbol'] for entry in data]
prices = [float(entry['price'].replace(',', '')) for entry in data]

# Define colors for bars
colors = ['skyblue', 'orange', 'green', 'red']

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(symbols, prices, color=colors)
plt.title('Prices of Stocks')
plt.xlabel('Symbols')
plt.ylabel('Prices (log scale)')
plt.xticks(rotation=45)
plt.yscale('log')  # Set y-axis to logarithmic scale
plt.tight_layout()
plt.show()

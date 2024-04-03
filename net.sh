#!/bin/bash

# Network Interface
network_interface="wlp1s0"  # Change this to your active network interface

# Function to get IP address
get_ip_address() {
    ip address show dev "$network_interface" | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"
}

# Function to get network speed
get_network_speed() {
    cat /sys/class/net/"$network_interface"/speed 2>/dev/null || echo "N/A"
}

# Function to get network traffic
get_network_traffic() {
    rx_old=$(cat "/sys/class/net/$network_interface/statistics/rx_bytes")
    tx_old=$(cat "/sys/class/net/$network_interface/statistics/tx_bytes")
    sleep 1
    rx_new=$(cat "/sys/class/net/$network_interface/statistics/rx_bytes")
    tx_new=$(cat "/sys/class/net/$network_interface/statistics/tx_bytes")
    rx_speed=$((rx_new - rx_old))
    tx_speed=$((tx_new - tx_old))
    echo "RX: $(numfmt --to=iec $rx_speed)/s TX: $(numfmt --to=iec $tx_speed)/s"
}

# Function to display network stats
display_network_stats() {
    echo "Network Interface: $network_interface"
    echo "IP Address: $(get_ip_address)"
    echo "Network Speed: $(get_network_speed) Mbps"
    echo "Network Traffic:"
    get_network_traffic
}

# Main function
main() {
    display_network_stats
}

# Run the main function
main

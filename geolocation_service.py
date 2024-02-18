import requests

def get_geolocation(ip_address):
    """
    Get geographical information for a given IP address using ipinfo.io.
    Returns a dictionary with location details.
    """
    api_key = "YOUR_API_KEY"  # Replace with your ipinfo.io API key or leave it empty for limited usage
    base_url = f"http://ipinfo.io/{ip_address}/json"

    if api_key:
        base_url += f"?token={api_key}"

    response = requests.get(base_url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch geolocation for IP address {ip_address}. Status code: {response.status_code}")
        return None

def main():
    # Example usage
    ip_address = "8.8.8.8"  # Replace with the actual IP address from your log data
    geolocation_info = get_geolocation(ip_address)

    if geolocation_info:
        print("Geographical information:")
        for key, value in geolocation_info.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()

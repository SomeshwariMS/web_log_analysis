# Web Log Analysis Project

This project analyzes web server logs to provide insights into page views, unique visitors, and more. Geolocation information is also included for each visitor.

## Project Structure

- **data**: Contains the web server log file (`web_access_log.txt`).
- **visualizations**: The folder where visualizations will be saved.
- **log_parser.py**: The main script for parsing logs and performing analysis.
- **geolocation_service.py**: Service to fetch geolocation information for IP addresses.
- **requirements.txt**: List of Python dependencies for the project.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

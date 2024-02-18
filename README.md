Web Log Analysis Project
This project analyzes web server logs to provide insights into page views, unique visitors, and more. Geolocation information is also included for each visitor.

Project Structure
data: Contains the web server log file (web_access_log.txt).
visualizations: The folder where visualizations will be saved.
log_parser.py: The main script for parsing logs and performing analysis.
geolocation_service.py: Service to fetch geolocation information for IP addresses.
requirements.txt: List of Python dependencies for the project.
Setup
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the analysis:

bash
Copy code
python log_parser.py
Analysis Results
The script will print analysis results, including total page views, unique visitors, and average response size. Visualizations, such as a bar chart of top pages by views, will be saved in the visualizations/ folder.

Geolocation Service
The project uses the ipinfo.io API for geolocation. Please obtain an API key from their website and replace "YOUR_API_KEY" in geolocation_service.py with your actual key.

License
This project is licensed under the MIT License - see the LICENSE file for details.

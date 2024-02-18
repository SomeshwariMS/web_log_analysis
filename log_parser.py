import re
from collections import defaultdict
import matplotlib.pyplot as plt
from geolocation_service import get_geolocation

def parse_log_entry(log_entry):
    """
    Parse a single log entry and extract relevant information.
    Returns a dictionary with parsed values.
    """
    log_pattern = re.compile(r'(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (\d+) (\d+)')
    match = log_pattern.match(log_entry)
    
    if match:
        return {
            'ip': match.group(1),
            'timestamp': match.group(4),
            'method': match.group(5),
            'url': match.group(6),
            'status_code': int(match.group(7)),
            'response_size': int(match.group(8))
        }
    else:
        return None

def get_geolocation_info(ip_address):
    """
    Get geolocation information for a given IP address.
    Returns a dictionary with location details.
    """
    return get_geolocation(ip_address)

def analyze_logs(parsed_logs):
    """
    Perform advanced analysis on the parsed logs.
    Returns a dictionary with analysis results.
    """
    analysis_results = {
        'total_page_views': len(parsed_logs),
        'unique_visitors': len(set(log['ip'] for log in parsed_logs)),
        'average_response_size': sum(log['response_size'] for log in parsed_logs) / len(parsed_logs)
    }

    # Count page views for each URL
    page_views_by_url = defaultdict(int)
    for log in parsed_logs:
        page_views_by_url[log['url']] += 1

    # Get the top 10 pages by page views
    top_pages_by_views = dict(sorted(page_views_by_url.items(), key=lambda x: x[1], reverse=True)[:10])

    analysis_results['top_pages_by_views'] = top_pages_by_views

    return analysis_results

def plot_top_pages_by_views(top_pages_by_views):
    """
    Create a bar chart to visualize the top pages by page views.
    """
    urls = list(top_pages_by_views.keys())
    page_views = list(top_pages_by_views.values())

    plt.bar(urls, page_views)
    plt.xlabel('URLs')
    plt.ylabel('Page Views')
    plt.title('Top Pages by Page Views')
    plt.xticks(rotation=45, ha='right')
    plt.show()

def main():
    # Read the log file
    log_file_path = 'data/web_access_log.txt'
    with open(log_file_path, 'r') as file:
        log_entries = file.readlines()

    # Parse log entries
    parsed_logs = [parse_log_entry(entry) for entry in log_entries]

    # Filter out None values (entries that couldn't be parsed)
    parsed_logs = [log for log in parsed_logs if log is not None]

    # Enrich logs with geolocation information
    for log in parsed_logs:
        geolocation_info = get_geolocation_info(log['ip'])
        log['geolocation'] = geolocation_info

    # Perform advanced analysis
    analysis_results = analyze_logs(parsed_logs)

    # Print analysis results
    for key, value in analysis_results.items():
        print(f'{key}: {value}')

    # Visualize top pages by views
    plot_top_pages_by_views(analysis_results['top_pages_by_views'])

if __name__ == "__main__":
    main()

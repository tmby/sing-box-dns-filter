import requests

urls = [
    "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt",
    "https://big.oisd.nl"
]

unique_lines = set()

def download_filters(urls):
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            print(f"Downloading {url} - Status Code: {response.status_code}")
            print(f"Original line count: {len(response.text.splitlines())}")
            filtered_lines = [line.strip() for line in response.text.splitlines() if line.strip() and not line.startswith('!')]
            print(f"Filtered line count: {len(filtered_lines)}")
            unique_lines.update(filtered_lines)
        except requests.RequestException as e:
            print(f"Download failed for {url}: {e}")

def save_to_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(unique_lines)) + '\n')

def main():
    download_filters(urls)
    save_to_file("temp_filters.txt")
    print(f"Temporary file 'temp_filters.txt' created with {len(unique_lines)} lines.")

if __name__ == "__main__":
    main()
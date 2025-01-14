# subfinder_everyday


This tool helps you track changes and additions to subdomains over time using **Subfinder**. Each time you run the tool, it only shows you the new subdomains that have been added since the last run. This allows you to easily determine what new subdomains have been added to your organization, for example, this week or today, compared to the previous week or day.

## Features

- **Track subdomain changes**: Instead of showing all subdomains every time, it only displays newly added subdomains.
- **Result storage**: Every time the tool runs, it saves the subdomains detected and compares them with future results.
- **Easy identification**: New subdomains are highlighted in green for easy identification

# Use : 
To provide input to the tool so that it searches for the target address you want, use the command: `nano subfinder_everyday.py` and change the value of `target_domain = "example.com"` on the last line.<img width="853" alt="Screenshot 2024-10-16 at 11 16 26 AM" src="https://github.com/user-attachments/assets/afd60430-605e-42df-a879-62726aead05a">



When you run the tool for the first time, make sure to run it at least twice so that all subdomains are fully collected from Subfinder. Keep running it until the tool no longer returns any new subdomains. After that, you can run the tool again tomorrow, and it will show you only the actual new subdomains.



Run the tool :‌
  python3 subfinder_everyday.py
 
## Prerequisites

- Python 3.x
- **Subfinder** must be installed on your system. You can install it via:
  ```bash
  go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest




## Author Information

- **GitHub**: [alimostafaeiorg](https://github.com/alimostafaeiorg)
- **Twitter**: [alimostafaeiorg](https://twitter.com/alimostafaeiorg)

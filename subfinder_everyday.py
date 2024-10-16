import subprocess
import os
import json



def run_subfinder(target):
    """Run Subfinder and return the found subdomains."""
    output_file = f"{target}_subdomains.txt"  
    
    subprocess.run(["subfinder", "-d", target, "-o", output_file, "-silent"])
    
    
    with open(output_file, 'r') as f:
        subdomains = f.read().splitlines()
    return set(subdomains) 


def print_author_info():
    author_info = "AliMostafaei | https://github.com/alimostafaeiorg "  
    print(f"\033[93m{author_info}\033[0m") 




def load_previous_results(target):
    """Load previously found subdomains from a file."""
    previous_file = f"{target}_previous_subdomains.json"
    if os.path.exists(previous_file):
        with open(previous_file, 'r') as f:
            return set(json.load(f))  
    return set()  

def save_current_results(target, subdomains):
    """Save the current found subdomains to a file."""
    current_file = f"{target}_previous_subdomains.json"
    with open(current_file, 'w') as f:
        json.dump(list(subdomains), f) 



def main(target):
    
    previous_results = load_previous_results(target)
    
    
    current_results = run_subfinder(target)

   
    new_subdomains = current_results - previous_results 
    if new_subdomains:
        print(f"\033[92m Subdomains added: \033[0m")
        for subdomain in new_subdomains:
            print(f"\033[92m{subdomain}\033[0m")
    else:
        print(f"\033[92m No new Subdomain\033[0m")

   
    save_current_results(target, current_results)

    print_author_info()



if __name__ == "__main__":
    target_domain = "dell.com" 
    main(target_domain)



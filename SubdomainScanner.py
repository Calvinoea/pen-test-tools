import requests


#domain to scan

domain = "google.com"


#read all subdomains

file = open("subdomains.txt")

#read all content

content = file.read()


subdomains = content.splitlines()


#list of subdomains discovered

discovered_subdomains = []

for subdomain in subdomains:

    # construct the url
    url = f"http://{subdomain}.{domain}"
    try:
        # if this produces an error, the subdomain does not exist
        requests.get(url)
    except requests.ConnectionError:
        # if the subdomain doesn't exist, pass, print nothing
        pass
    else:
        print("[+] Discovered subdomain:", url)
        # append the discovered subdomain to our list
        discovered_subdomains.append(url)

# save the discovered subdomains into a file
with open("discovered_subdomains.txt", "w") as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)

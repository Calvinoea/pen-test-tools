import whois

sites = ["facebook.com", "spotify.com", "instagram.com", "meta.com", "whatsapp.com"]

companies = [whois.whois(s).org for s in sites]
creation_dates = [whois.whois(s).creation_date for s in sites]


print(companies)
print(creation_dates)

print(sites[creation_dates.index(min(creation_dates))])


emails = [whois.whois(s).emails for s in sites]

print(emails)

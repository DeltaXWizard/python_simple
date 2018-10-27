import whois

def on_ready():
    """Whois Registrar Lookup in Python"""
    IP = input("Enter a domain name or IP you want to look up: ")
    # we combat result with possible errors.
    try:
        obj = whois.whois(IP)
        print(obj)
    except whois.parser.PywhoisError as e: #conflicts possible IPs.
        print ("There is no match for this specific domain/IP.")

on_ready() #booting upon execution

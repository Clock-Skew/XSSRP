import requests

def send_through_proxy(url, payload, proxy_address):
    """
    Send a request through a specified proxy.
    """
    proxies = {
        "http": proxy_address,
        "https": proxy_address,
    }
    # Example of a simple GET request with the payload in the query string
    response = requests.get(f"{url}?q={payload}", proxies=proxies)
    return response

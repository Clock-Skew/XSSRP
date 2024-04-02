import requests

def test_payload(url, payload):
    """
    Tests a given payload on a URL.

    :param url: The URL to test the payload on.
    :param payload: The XSS payload to test.
    :return: None
    """
    # Example of appending the payload as a query parameter
    target = f"{url}?q={payload}"
    try:
        response = requests.get(target)
        if payload in response.text:
            print(f"Possible XSS detected at {target}")
            # Further logic to confirm if the payload execution was successful
            # This could be improved by checking for specific execution indicators
    except requests.RequestException as e:
        print(f"Request failed: {e}")

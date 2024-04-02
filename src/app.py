import sys
import click
import signal
from spider import XSSSpider
from test_xss import test_payload
from scrapy.crawler import CrawlerProcess

# Define a signal handler function
def signal_handler(signal, frame):
    print('\nExecution stopped by user. Cleaning up...')
    sys.exit(0)

# Register the signal handler for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

@click.command()
@click.option('--url', help='Target URL to scan and test for XSS.')
def main(url):
    # No need for a try-except block for KeyboardInterrupt here
    # as signal handling is now taken care of by the signal_handler function
    process = CrawlerProcess()
    process.crawl(XSSSpider, domain=url)
    process.start()  # This will spider the website

    # For each identified form or URL, test payloads
    payloads = open('../payloads/payloads.txt').read().splitlines()
    for payload in payloads:
        test_payload(url, payload)

if __name__ == '__main__':
    main()


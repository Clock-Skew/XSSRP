import sys
import click
from spider import XSSSpider
from test_xss import test_payload
from scrapy.crawler import CrawlerProcess

@click.command()
@click.option('--url', help='Target URL to scan and test for XSS.')
def main(url):
    process = CrawlerProcess()
    process.crawl(XSSSpider, domain=url)
    process.start()  # This will spider the website

    # For each identified form or URL, test payloads
    payloads = open('../payloads/payloads.txt').read().splitlines()
    for payload in payloads:
        test_payload(url, payload)
        
            except KeyboardInterrupt:
        print("\nExecution stopped by user. Cleaning up...")
        # Perform any cleanup here
        sys.exit(0)

if __name__ == '__main__':
    main()

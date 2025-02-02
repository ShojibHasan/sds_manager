from celery import shared_task
import subprocess

@shared_task
def scrape_hotels(data):
    subprocess.run(["scrapy", "crawl", "booking"])
    subprocess.run(["scrapy", "crawl", "agoda"])

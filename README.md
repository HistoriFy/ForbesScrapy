# ForbesScrapy
Crawling Top 800 Best Employers Data from Forbes.com using Scrapy.

## Introduction
Details about the all 800 entries present in [World's Best Employers](https://www.forbes.com/lists/worlds-best-employers/?sh=5dc799fd1e0c) Data hosted by Forbes was crawled using [Scrapy](https://scrapy.org/), sorted out rank wise and then stored in a json file named 

The same spider is then used to crawl revelant data of top 20 companies by rank through their profile links fetched from the original list. Result is again stored in another json file named **company.json** (Just with a different parser function this time)

## Requirements 

Please run the project folder in a virtual enviroment with the requirements.txt installed first to avoid any issues.


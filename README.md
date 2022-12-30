# ForbesScrapy
Crawling Top 800 Best Employers Data from Forbes.com using Scrapy.

## Introduction
Details about the all 800 entries present in [World's Best Employers](https://www.forbes.com/lists/worlds-best-employers/?sh=5dc799fd1e0c) Data hosted by Forbes was crawled using [Scrapy](https://scrapy.org/), sorted out rank wise and then stored in a json file named  **forbes1.json**

The same spider is then used to crawl revelant data of top 20 companies by rank through their profile links fetched from the original list. Result is again stored in another json file named **company.json** (Just with a different parser function this time)

Spider is named **spider1.py** in the spiders folder.

To simply crawl data at once, run the following command in terminal:
```sh
scrapy crawl spider1
```

Data will be stored in the parent folder.

## Requirements 

Please run the project folder in a virtual enviroment with the requirements.txt installed first to avoid any issues.

Libraries specifically used are:

- [Scrapy](https://scrapy.org/) - v2.6.2

  ```sh
  pip install scrapy
  ```
  
- [Fake-Useragent](https://github.com/fake-useragent/fake-useragent) - v1.1.1

  
  ```sh
  pip install fake-useragent
  ```

  Or if you have multiple Python / pip versions installed, use `pip3`:

  ```sh
  pip3 install fake-useragent
  ```

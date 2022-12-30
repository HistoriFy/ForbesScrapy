import scrapy
from fake_useragent import UserAgent
import json

#please install the libraries from requirements.txt in a virtual env for smooth run.

class forbesspider(scrapy.Spider):
    name = 'spider1'
    u=UserAgent()
    top20 = [] #empty list with global scope to store data for second task
    allowed_domains = ['forbes.com']
    start_urls = ['https://www.forbes.com/lists/worlds-best-employers/?sh=2763362f1e0c',]


    def start_requests(self): #adding random useragent for each request to decrease the changes of getting blocked for multiple requests from a single useragent
        url='https://www.forbes.com/lists/worlds-best-employers/?sh=520fb0c11e0c'
        headers={"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate, br","accept-language":"en-US,en;q=0.9,de;q=0.8","user-agent":self.u.random}
        yield scrapy.Request(url,callback=self.parse,method='GET',headers=headers)



    def parse(self, response):

        data=[]          #empty list to store data for first task

        companies=[]     #empty list for storing rank and link for parsing in task 2's parser
        
        #Fetching all details as a list with 800 elements by searching the common class name for all 800 details by Xpath Query

        for company in response.xpath('//a[contains(@class,"premiumProfile")]'):
            

            Rank=company.xpath('./div[contains(@class,"rank")]/text()').get().strip(".")
            Name=company.xpath('./div[contains(@class,"name")]/text()').get()
            Industries=company.xpath('./div[contains(@class,"industry")]/text()').get()
            Country=company.xpath('./div[contains(@class,"country")]/text()').get()
            Employees=company.xpath('./div[contains(@class,"employees")]/text()').get()
            Link=company.css('::attr(href)').get()

            #Adding links for premium companies whose profle links aren't present normally with href tag

            if Link == None:
                Link=f'https://www.forbes.com/companies/{company.css("::attr(uri)").get()}/?list=worlds-best-employers'

            if int(Rank) <=20:
                companies.append([Rank,Link])

                #Creating the list for the second task parser

            #companies with no data for employees class will have null automatically for them
            
            



            

            data.append({'rank':Rank,'name':Name,'industry':Industries,'country':Country,'employees':Employees,'page':Link})


        #Creating a dictionary of those values and writing it down it in a forbes1.json file.
        with open('forbes1.json','w',encoding='utf-8') as file:
            json.dump(data, file)

        for b in companies:
            c_rank,c_link=b
            yield scrapy.Request(c_link,callback=self.parse2,method='GET',meta={"rank":c_rank}) 

    def parse2(self, response):
        c_rank=response.request.meta["rank"]  
        name= response.css('h1.listuser-header__name::text').get()  #Unique class names same for all 20 pages hence using css here was a better option
        stock_symbol=response.css('div.listuser-ticker::text').get()
        stock_price=response.css('div.profile-info__item-value::text').get()
        founded=response.xpath("//span[@class='profile-stats__title' and text()='Founded']/following-sibling::span/span/text()").get()
        headquarters=response.xpath("//span[@class='profile-stats__title' and text()='Headquarters']/following-sibling::span/span/text()").get()
        ceo=response.xpath("//span[@class='profile-stats__title' and text()='Chief Executive Officer']/following-sibling::span/span/text()").get()

        #Exact path of the sibling or son classes was fetched by xpath again. Same for all 20 Pages

        if ceo == None:
            ceo=response.xpath("//span[@class='profile-stats__title' and text()='Executive Chairman']/following-sibling::span/span/text()").get()

        #Some company(s) have Executive Chairman instead of CEO

        _2022_Rev=response.xpath("//div[@class='listuser-financial-data' and @data-index='0']//div[text()='Revenue']/following-sibling::div/text()").get()
        _2022_Assets=response.xpath("//div[@class='listuser-financial-data' and @data-index='0']//div[text()='Assets']/following-sibling::div/text()").get()
        _2022_Profits=response.xpath("//div[@class='listuser-financial-data' and @data-index='0']//div[text()='Profits']/following-sibling::div/text()").get()

        _2021_Rev=response.xpath("//div[@class='listuser-financial-data hidden' and @data-index='1']//div[text()='Revenue']/following-sibling::div/text()").get()
        _2021_Assets=response.xpath("//div[@class='listuser-financial-data hidden' and @data-index='1']//div[text()='Assets']/following-sibling::div/text()").get()
        _2021_Profits=response.xpath("//div[@class='listuser-financial-data hidden' and @data-index='1']//div[text()='Profits']/following-sibling::div/text()").get()
        
        #past two year finanical data is majorly parsed in parser for task 2

        self.top20.append({"Rank":c_rank,"name":name,"stock_symbol":stock_symbol,"stock_price":stock_price,"founded":founded,"headquarters":headquarters,"ceo":ceo,"_2022_Rev":_2022_Rev,"_2022_Assets":_2022_Assets,"_2022_Profits":_2022_Profits,"_2021_Rev":_2021_Rev,"_2021_Assets":_2021_Assets,"_2021_Profits":_2021_Profits})

        #again like task 1, json file named company.json in write mode is created and top 20 companies is written into it

        with open('company.json','w',encoding='utf-8') as f:
            json.dump(self.top20,f)


        
        




    



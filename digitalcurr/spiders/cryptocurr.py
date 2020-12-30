import scrapy
from ..items import DigitalcurrItem

class CryptocurrSpider(scrapy.Spider):
    name = 'cryptocurr'
    # allowed_domains = ['https://coinmarketcap.com/all/views/all/']
    # start_urls = ['http://https://coinmarketcap.com/all/views/all//']

    def start_requests(self):
        url = "https://coinmarketcap.com/all/views/all/"
        yield scrapy.Request(url=url, callback=self.parse) 



    def parse(self, response):
        table = response.xpath("//tbody/tr")
        for row in table:
            item = DigitalcurrItem()

            item["rank"] = row.xpath(".//td[contains(@class, 'cmc-table__cell--sort-by__rank')]//div//text()").extract_first(),
            item["name"] = row.xpath(".//td[contains(@class, 'cmc-table__cell--sort-by__name')]//text()").extract_first(),
            item["symbol"] = row.xpath(".//td[contains(@class, 'cmc-table__cell--sort-by__symbol')]//text()").extract_first()
            item["market_cap"] = row.xpath(".//td[contains(@class, 'cmc-table__cell--sort-by__market-cap')]//text()").extract_first()
            item["price"] = row.xpath(".//td[contains(@class, 'cmc-table__cell--sort-by__price')]//text()").extract_first()
            item["circulating_supply"] = row.xpath(".//td[contains(@class, 'circulating-supply')]//text()").extract_first()
            item["volume_24h"] = row.xpath(".//td[contains(@class, 'volume-24-h')]//text()").extract_first()



            yield item


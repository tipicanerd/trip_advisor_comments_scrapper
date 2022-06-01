import scrapy
import urllib.parse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from tripadvisor.items import TripadvisorItem



#24 y 25 de junio
"""
Mexcaltitán NO HAY HOTELES
ElRosarito NO HAY HOTELES
"""
class tripAdvisorSpider(CrawlSpider):
	name = 'tripadvisor'
	item_count = 0
	allowed_domain = ['https://www.tripadvisor.com.mx']
	pages = 0
	start_urls = [
	"https://www.tripadvisor.com/Hotels-g150777-Todos_Santos_Baja_California-Hotels.html",
	"https://www.tripadvisor.com/Hotels-g150772-Loreto_Baja_California-Hotels.html",
	"https://www.tripadvisor.com/Hotels-g6368948-Isla_Aguada_Yucatan_Peninsula-Hotels.html",
	"https://www.tripadvisor.com/Hotels-g445056-Sayulita_Pacific_Coast-Hotels.html",
	"https://www.tripadvisor.com/Hotels-g1767159-Compostela_Pacific_Coast-Hotels.html",
	"https://www.tripadvisor.com/Hotels-g658264-Mazunte_Southern_Mexico-Hotels.html",
	"https://www.tripadvisor.com/Hotels-g1202648-Bacalar_Yucatan_Peninsula-Hotels.html",
	"https://www.tripadvisor.com/Hotels-g150810-Isla_Mujeres_Yucatan_Peninsula-Hotels.html",
	"https://www.tripadvisor.com/Hotels-g150813-Tulum_Yucatan_Peninsula-Hotels.html",
	"https://www.tripadvisor.com/Hotels-g1202651-Papantla_Central_Mexico_and_Gulf_Coast-Hotels.html",
	"https://www.tripadvisor.com/Hotels-g2550231-Sisal_Yucatan_Peninsula-Hotels.html"
	]
	
	rules = {
		Rule(LinkExtractor(
			allow = (),
			restrict_xpaths = ('//div[contains(@class,"listing_title")]/a')
			),
			callback = 'parse_item',
		),
		Rule(LinkExtractor(
			allow=(),
			restrict_xpaths= ('//div[@class="unified ui_pagination standard_pagination ui_section listFooter"]/a[@class="nav next ui_button primary"]')
			)
		),
		Rule(LinkExtractor(
			allow = (),
			restrict_xpaths = ('//a[@class="pageNum"]'),
			process_value = lambda x: urllib.parse.urljoin('https://www.tripadvisor.com.mx',x)
			),
			callback = 'parse_item'
		)
	}

	

	def parse_item(self,response):
		city= response.xpath('/html/body/div[1]/div/div[2]/div[6]/div/div/div/div[2]/ul/li[4]/a/span/text()').extract()
		name= response.xpath('//h1/text()').extract_first()
		stars= response.xpath('//div[@class="drcGn _R MC S4 _a H"]/span/*[local-name()="svg"]/@aria-label').extract()
		rating= response.xpath('//span[@class="bvcwU P"]/text()').extract_first()
		price= response.xpath('//div[@class="vyNCd b Wi"]/text()').extract()
		quality_price= response.xpath('//div[@class="cVJkH"]/span[2]/text()').extract()

		if len(quality_price)>0:
			quality_price = quality_price[-1]

		url = response.url

		n = len(response.xpath('//div[@class="cqoFv _T"]'))

		for i in range(n):
			ta_item = TripadvisorItem()

			ta_item['city'] = city
			ta_item['name'] = name
			ta_item['stars'] = stars
			ta_item['rating'] = rating
			ta_item['price'] = price
			ta_item['quality_price'] = quality_price
			ta_item['url'] = url

			ta_item['score'] = response.xpath('//div[@class="cqoFv _T"]/div/div[@class="emWez F1"]/span/@class').extract()[i]
			ta_item['comment'] = response.xpath('//div[@class="cqoFv _T"]/div[@class="dovOW"]/div/div[@class="pIRBV _T"]/q/span/text()').extract()[i]


			yield ta_item

		
		

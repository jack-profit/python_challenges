import scrapy
from ..items import RepositoryItem


class RepositorySpider(scrapy.Spider):
    name = 'repository'
    start_urls = ['https://github.com/shiyanlou?tab=repositories']

    def parse(self, response):
        for target in response.css('li.col-12'):
            item = RepositoryItem({
                'name': target.css('h3 a::text').extract_first().strip(),
                'update_time': target.xpath('.//relative-time/@datetime'
                        ).extract_first(),
            })
            target_url = target.css('h3 a::attr(href)').extract_first()
            request_son = scrapy.Request(
                    response.urljoin(target_url), self.parse_son)
            request_son.meta['main'] = item # jiang yi huo qu dao de xin xi xie dai zhe
            yield request_son

    def parse_son(self, response):
        main = response.meta['main']
        # zai xiang qing ye cai ji sheng yu xin xi
        main['commits'] = response.xpath('//ul[@class="numbers-summary"]/li[1]').xpath('.//span[contains(@class, "num")]/text()').extract_first().strip()
        main['branches'] = response.xpath('//ul[@class="numbers-summary"]/li[2]').xpath('.//span[contains(@class, "num")]/text()').extract_first().strip()
        main['releases'] = response.xpath('//ul[@class="numbers-summary"]/li[3]').xpath('.//span[contains(@class, "num")]/text()').extract_first().strip()
        yield main

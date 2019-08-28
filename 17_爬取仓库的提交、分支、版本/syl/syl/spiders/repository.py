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
        # 获取page连接元素
        next_page_url = response.css('div.paginate-container a::attr(href)')
        '''
        for next_page in response.css('div.paginate-container a::attr(href)'):
            a_str = next_page.xpath('.//a/text()').extract_first().strip()
            if a_str == 'Next':
                url = next_page.xpath('.//a/@href').extract_first()
        '''
        if len(next_page_url) == 2:
            # 如果包含两个链接，就进入'下一页'
            yield response.follow(next_page_url[-1], self.parse)
        else:
            # 首页和最后一页只包含一个链接
            a_str = response.css('div.paginate-container a::text'
                    ).extract_first().strip()
            if a_str == 'Next':
                # 如果这个链接是'Next'，则进入
                url = response.css('div.paginate-container a::attr(href)'
                        ).extract_first()
                yield scrapy.Request(url, self.parse)

    def parse_son(self, response):
        main = response.meta['main']
        # 获取提交数 
        commits = response.xpath('//ul[@class="numbers-summary"]/li[1]'
                ).xpath('.//span[contains(@class, "num")]/text()').extract_first()
        if commits:
            # 仓库不为空
            main['commits'] = commits.strip()
            main['branches'] = response.xpath('//ul[@class="numbers-summary"]/li[2]'
                    ).xpath('.//span[contains(@class, "num")]/text()'
                    ).extract_first().strip()
            main['releases'] = response.xpath('//ul[@class="numbers-summary"]/li[3]'
                    ).xpath('.//span[contains(@class, "num")]/text()'
                    ).extract_first().strip()
        yield main

# _*_ coding:utf-8 _*_
import scrapy

class CoursesFollowSpider(scrapy.Spider):
    name = 'courses_follow'
    start_urls = ['https://shiyanlou.com/courses/63']

    def parse(self, response):
        yield {
                'name': response.css('h1.course-title::text').extract_first().strip(),
                'author': response.css('p.teacher-info span::text').extract_first()
            }

        for url in response.css('div.course-item-box a::attr(href)').extract():
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse)


class CoursesFollowSpiders(scrapy.Spider):
    name = 'courses_follows'
    start_urls = ['https://www.shiyanlou.com/courses/63']

    def parse(self, response):
        yield {
                'name': response.css('h1,course-title::text').extract_first().strip(),
                'author': response.css('p.teacher-info span::text').extract_first()
                }
        for url in response.css('div.course-item-box a::attr(href)'):
            yield response.follow(url, callback=self.parse)

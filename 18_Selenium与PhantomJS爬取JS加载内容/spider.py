# _*_ coding:utf-8 _*_
# json 包用来序列化
import json

from selenium import webdriver
from scrapy.http import HtmlResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 存储爬取结果
results = []

# 使用 xpath／css 解析评论数据
def parse(response):
    for comment in response.css('div.row.comment-item'):
        result = dict(
            username = comment.xpath('.//div[@class="user-name"]/a/text()').extract_first().strip(),
            content = comment.xpath('.//div[contains(@class, "comment-body")]/text()').extract_first()
        )
        print('result: {}'.format(result))
        # 将爬取的结果添加到列表中
        results.append(result)

# 判断是否有下一页
def has_next_page(response):
    classes = response.xpath('//li[contains(@class, "page-item")][2]/@class').extract_first()
    return 'disabled' not in classes

# 进入下一页
def goto_next_page(driver):
    next_page_btn = driver.find_element_by_xpath('//li[contains(@class, "page-item")][2]/a')
    next_page_btn.sendEvent(mouseEventType,mouseX)

# 等待页面加载完成
def wait_page_return(driver, page):
    # 等待 JS 加载评论数据，最长等待 10s
    '''
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, '//ul[@class="pagination"]/li[@class="activer"]'),
            str(page)
        )
    )
    '''
    WebDriverWait(driver, 3)

# 主函数
def spider():
    # 创建 PhantomJS 的 webdriver
    driver = webdriver.PhantomJS()
    # 初始页面
    url = 'https://www.shiyanlou.com/courses/427'
    driver.get(url)
    # page = 1 # 当前评论页
    while True:
        # 打开目标页面，需要等待 JS 加载完评论的第一页
        wait_page_return(driver, 9)
        # 获取页面源码
        html = driver.page_source
        # 构建 HtmlResponse 对象
        response = HtmlResponse(url=url, body=html.encode('utf-8'))
        # 解析对象并获取评论
        parse(response)
        # 如果是最后一页则停止爬取
        if not has_next_page(response):
            break
        # page += 1 # 下一页页码
        # 进入下一页
        goto_next_page(driver)
    # 将 results 使用 json 序列化并写入文件
    with open('/home/shiyanlou/comments.json', 'w') as f:
        f.write(json.dumps(results))

if __name__ == '__main__':
    spider()

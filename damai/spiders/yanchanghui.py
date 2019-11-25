# -*- coding: utf-8 -*-

from scrapy import Spider,Request
from urllib.parse import urlencode
import json
from damai.items import YanItem
from damai.settings import KEY_WORD

class YanchanghuiSpider(Spider):
    name = 'yanchanghui'
    allowed_domains = ['search.damai.cn']
    

    def start_requests(self):#没有在定义start_url是因为可以写此函数来定义开始的url并且可以根据搜索的内容不同和结果页数的不同来随心定制
            base_url = 'https://search.damai.cn/searchajax.html?'
            params = {
            'keyword': self.settings.get('KEY_WORD'),
            'ct':'' ,
            'ctl': '',
            'sctl':'' ,
            'tsg': 0,
            'st': '',
            'et': '',
            'order': 0,
            'pageSize': 30,
            'currPage':1,
            'tn':''
            }
            params = urlencode(params)
            url = base_url + params
            yield Request(url,self.parse_url) 
            
    def parse_url(self,response):
        results = json.loads(response.text)
        total_page = results["pageData"]["totalPage"]#从此处可以知道搜索到结果的总共页数 
        base_url = 'https://search.damai.cn/searchajax.html?'
        for page in range(0,total_page + 1):#++++页数应该是从1开始的，但是如果循环从1开始会不解析第一页++++
            params = {
            'keyword': self.settings.get('KEY_WORD'),
            'ct':'' ,
            'ctl': '',
            'sctl':'' ,
            'tsg': 0,
            'st': '',
            'et': '',
            'order': 0,
            'pageSize': 30,
            'currPage':page,
            'tn':''
            }
            params = urlencode(params)
            url = base_url + params
            yield Request(url = url, callback=self.parse)
        
        
    def parse(self,response):#此处可以添加任何想要爬取的字段，但是也要从items文件中对应添加
        results = json.loads(response.text)
        datas = results["pageData"]["resultData"]#得到的结果先过滤，这样循环的次数会少一些
        for data in datas:
            item = YanItem()
            item['name'] = data["nameNoHtml"]
            item['actors'] = data["actors"]
            item['showtime'] = data["showtime"]
            item['city'] = data["cityname"]
            yield item
        

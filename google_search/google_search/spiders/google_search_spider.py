# -*- coding: utf-8 -*-
import re
from urllib import urlencode
import logging
import urlparse

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest
from google_search.items import GoogleSearchItem


class GoogleSearchSpider(CrawlSpider):
    name = 'google_search'
    allowed_domains = ['www.google.com']

    def __init__(self, q):
        q_list = re.split(ur',', q)
        search_str = '+'.join(q_list)
        logging.warning('q: %s search_str: %s', q, search_str)
        self.start_urls = ['http://www.google.com/search?q=' + search_str]
        self.q_list = q_list

        super(CrawlSpider, self).__init__()

        self._compile_rules()

    def parse_start_url(self, response):
        logging.warning('url: %s meta: %s', response.url, response.meta)
        hxs = HtmlXPathSelector(response)

        records = hxs.xpath('//li[@class="g"]')
        for r in records:
            href = r.xpath('.//h3/a/@href').extract()[0]
            logging.warning('href: %s', href)
            # if not len(href):
            #    continue

            # href = href[0]
            url_struct = urlparse.urlparse(href)
            path = url_struct.path

            logging.warning('href: %s url_struct: %s path: %s', href, url_struct, path)

            if path != '/url':
                continue

            qs = url_struct.query
            qs_struct = urlparse.parse_qs(qs)
            url = qs_struct['q'][0]

            names = r.xpath('./h3/a').extract()
            name = ''.join(names)
            name = re.sub('<.*?>', '', name)

            item = GoogleSearchItem()

            item['ref_url'] = response.url
            item['url'] = url
            item['name'] = name

            yield item

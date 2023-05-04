import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep in response.css(
                '#numerical-index > table > tbody > tr > td > a::attr(href)'
        ).getall():
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css(
            '#pep-content > h1::text'
        ).get().split(' – ', 1)
        number = int(number.replace('PEP ', ''))
        status = response.css(
            '#pep-content > dl > dt:contains("Status") + dd > abbr::text'
        ).get()

        yield PepParseItem(
            number=number,
            name=name,
            status=status,
        )

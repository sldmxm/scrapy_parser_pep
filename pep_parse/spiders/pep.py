import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']
    # тесты требуют явного указания 'https://peps.python.org/' в start_urls
    # можно что-то такое, хотя оно, кажется, менее читаемо
    allowed_domains = [url.split('/')[2] for url in start_urls]

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

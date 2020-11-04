import scrapy


class EvansSpider(scrapy.Spider):
    name = "evans"
    start_urls = ["https://www.evanscycles.com/bikes/folding-bikes"]

    def parse(self, response, **kwargs):
        for product in response.css("li[li-productid]"):
            product_name = product.attrib["li-name"]
            url = "https://www.evanscycles.com{url}".format(
                url=product.attrib["li-url"]
            )
            yield {
                "product_name": product_name,
                "url": url,
            }

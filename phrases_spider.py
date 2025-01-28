import scrapy


class Phrases(scrapy.Spider):
    name = "phrases"
    allowed_domains = ["frazite.com"]
    start_urls = ["https://frazite.com/"]

    def parse(self, response, **kwargs):
        row = response.css("tr")
        data = row.css("td")
        title = response.css("title::text").get()
        first_phrase = data.css("strong a::attr('href')::text").get()

        try:
            yield {
                "Title": title,
                "First_phrase": first_phrase
            }

        except:
            raise Exception("Text could not be parsed")


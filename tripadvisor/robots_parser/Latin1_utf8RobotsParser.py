from scrapy.robotstxt import RobotParser
from scrapy.utils.python import to_unicode


class Latin1_utf8RobotsParser(RobotParser):
    def __init__(self, robotstxt_body, spider):
        from protego import Protego
        self.spider = spider

        # Default decoding is to a String object ('utf-8')
        robotstxt_body = robotstxt_body.decode('iso-8859-1')

        self.rp = Protego.parse(robotstxt_body)

    @classmethod
    def from_crawler(cls, crawler, robotstxt_body):
        spider = None if not crawler else crawler.spider
        o = cls(robotstxt_body, spider)
        return o

    def allowed(self, url, user_agent):
        user_agent = to_unicode(user_agent)
        url = to_unicode(url)
        return self.rp.can_fetch(url, user_agent)
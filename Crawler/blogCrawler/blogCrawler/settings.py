from dotenv import load_dotenv
import os

# Scrapy settings for testpj project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


load_dotenv()

BOT_NAME = "blogCrawler"

SPIDER_MODULES = ["blogCrawler.spiders"]
NEWSPIDER_MODULE = "blogCrawler.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 1
RETRY_TIME = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ko",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    "blogCrawler.middlewares.BlogSpiderMiddleware": 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "testpj.middlewares.TestpjDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "blogCrawler.pipelines.NaverPipeline": 500,
}



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEED_EXPORT_FIELDS = ["media","keyword", 'date', "url", "title",
                      "content", "comment", "writer", "view"]

LOG_LEVEL = "ERROR"
LOG_FORMAT = '%(levelname)s: %(message)s'


# ELASTICSEARCH_SERVER = 'http://10.7.18.2'
# ELASTICSEARCH_PORT = 9200
# MARIADB_HOST = '10.7.18.2'
# MARIADB_PORT = 3306
# MARIADB_USERNM = 'root'
# MARIADB_PASSWD = 'wizontech0418'
# MARIADB_DBNM = 'rissue'
# LOG_PATH = '/applog/crawler/naverBlog/'

ELASTICSEARCH_SERVER = os.environ.get('ELASTICSEARCH_SERVER')
ELASTICSEARCH_PORT = int(os.environ.get('ELASTICSEARCH_PORT'))
MARIADB_HOST = os.environ.get('MARIADB_HOST')
MARIADB_PORT = int(os.environ.get('MARIADB_PORT'))
MARIADB_USERNM = os.environ.get('MARIADB_USERNM')
MARIADB_PASSWD = os.environ.get('MARIADB_PASSWD')
MARIADB_DBNM = os.environ.get('MARIADB_DBNM')
LOG_PATH = f'{os.environ.get("LOG_PATH")}naverBlog/'



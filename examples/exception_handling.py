from pyalux import Alux
from pyalux.exceptions import InvalidTagException, InvalidCategoryException, \
    NoArticlesFoundException, UnknownUrlException, \
    UnknownPageFormatException, BadPostException

invalid_string = "sjbaghjjlhiGH K"

try:
    for post in Alux.search(invalid_string):
        pass
except NoArticlesFoundException:
    print("no articles")

try:
    for post in Alux.search_by_category(invalid_string):
        pass
except InvalidCategoryException:
    print("unknown category")

try:
    for post in Alux.search_by_tag(invalid_string):
        pass
except InvalidTagException:
    print("unknown tag")

try:
    for post in Alux.crawl("https://www.alux.com/" + invalid_string):
        pass
except UnknownUrlException:
    print("that is not an alux url")

try:
    for post in Alux.get_posts("https://www.alux.com/" + invalid_string):
        pass
except UnknownPageFormatException:
    print("bad page schema")

try:
    for post in Alux.parse_post("https://www.alux.com/" + invalid_string):
        pass
except BadPostException:
    print("that is not an alux post url")
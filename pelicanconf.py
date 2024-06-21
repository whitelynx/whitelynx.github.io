import re

AUTHOR = 'David H. Bronke'
SITENAME = 'David H. Bronke'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/whitelynx/"),
    ("GitLab", "https://gitlab.com/whitelynx/"),
    ("OSDN", "https://osdn.net/users/whitelynx/"),
    ("CodePen", "https://codepen.io/whitelynx/"),
    ("Hackaday", "https://hackaday.io/whitelynx"),
    ("Stack Overflow", "https://stackoverflow.com/users/677694/codermonkeyfuel"),
    ("Keybase", "https://keybase.io/codermonkeyfuel"),
    ("LinkedIn", "https://www.linkedin.com/in/davidbronke/"),
    ("Xing", "https://www.xing.com/profile/David_Bronke"),
    ("SoundCloud", "https://soundcloud.com/dbronke"),
    ("YouTube", "https://www.youtube.com/channel/UCv0t_sk50kSYLfl_7j16Gkw"),
)

MENUITEMS = (
    ("About", SITEURL),
    ("Projects", f"{SITEURL}/projects"),
    ("Résumé", f"{SITEURL}/resume"),
    ("Social", f"{SITEURL}/social"),
)

DEFAULT_PAGINATION = False

DEFAULT_DATE = 'fs'

THEME = "themes/lynx"

PAGE_ORDER_BY = 'order'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.sane_lists': {},
        'markdown.extensions.smarty': {},
        'mdx_headdown': {'offset': 1},
    },
    'output_format': 'html5',
}


comment_re = re.compile(r'<!--.*?-->', re.DOTALL)


# Custom filter method
def remove_html_comments(s):
    """A non-optimal implementation of a regex filter"""
    return comment_re.sub('', s)


JINJA_FILTERS = {
    'remove_html_comments': remove_html_comments,
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

AUTHOR = 'MedSecure'
SITENAME = 'Sphinx'
SITEURL = "https://sfinx.kozow.com"
LOAD_CONTENT_CACHE = False
# all the following settings are *optional*

# Site Logo
SITELOGO = ''

# HTML metadata
SITEDESCRIPTION = 'Ghost Shell, lurking throughs the realm of electronic device, find a way to break in while you being the watcher of my work. follow me alonng the journey, To the Abyss.'

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True
DARK_LIGHT_SWITCHING_OFF = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
PATH = 'content'
ARTICLE_PATHS = ['portswigger','htb']
DATE_FORMAT = { 'en': '%d %m %Y'}
DEFAULT_DATE_FORMAT = '%d %m %Y'
ARTICLE_URL = '{date:%Y}/{date:%-m}/{date:%-d}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('PortSwigger', ARTICLE_URL, ARTICLE_SAVE_AS),
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
)

# additional menu items
MENUITEMS = (
    ('GitHub', 'https://github.com/Medaz-Sploit'),
)

# example pagination pattern
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)



THEME = "/Users/slimanaz/pelican-themes/blue-penguin-dark"

TIMEZONE = 'Africa/Casablanca'

DEFAULT_LANG = 'en'
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

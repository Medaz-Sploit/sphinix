AUTHOR = 'MedSecure'
SITENAME = 'Sphinx'
SITEURL = "https://sfinx.kozow.com"
# all the following settings are *optional*

# Site Logo
SITELOGO = ''

# HTML metadata
SITEDESCRIPTION = 'Ghost Shell, lurking throughs the realm of electronic device, find a way to break in while you being the watcher of my work. follow me alonng the journey, To the Abyss.'

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly"
    }
}

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True
DARK_LIGHT_SWITCHING_OFF = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
PATH = 'content'
INDEX_SAVE_AS = 'homepage.html'
ARTICLE_URL = 'article/{slug}.html'
ARTICLE_SAVE_AS = 'article/{slug}.html'
CATEGORIES_URL     = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    ('Categories', CATEGORIES_URL, CATEGORIES_SAVE_AS),
)

# additional menu items
MENUITEMS = (
    ('GitHub', 'https://github.com/Medaz-Sploit'),
    ('PortSwigger', 'https://sfinx.kozow.com/category/portswigger.html'),
    ('HTB', 'https://sfinx.kozow.com/category/htb.html'),
    ('OSCP', 'https://sfinx.kozow.com/category/oscp.html'),
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

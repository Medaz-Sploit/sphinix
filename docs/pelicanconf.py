AUTHOR = 'MedSecure'
SITENAME = 'Sphinx'
SITEURL = "https://sfinx.kozow.com"

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

# use those if you want pelican standard pages to appear in your menu
# additional menu items
MENUITEMS = (
    ('GitHub', 'https://github.com/Medaz-Sploit'),
)

SOCIAL = (
    ("twitter", "http://twitter.com/ametaireau"),
    ("lastfm", "http://lastfm.com/user/akounet"),
    ("github", "http://github.com/ametaireau"),
)

# example pagination pattern
PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)


PATH = "content"

THEME = "/home/kali/pelican-themes/blue-penguin-dark"

TIMEZONE = 'Africa/Casablanca'

DEFAULT_LANG = 'en'
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

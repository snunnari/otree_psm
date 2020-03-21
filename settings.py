from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {
    'real_world_currency_per_point': 1.00,
    'participation_fee': 0.00,
    'doc': "",
}

SESSION_CONFIGS = [

    {
        'name': 'willingness_to_act',
        'display_name': "Willingness-To-Act Questions",
        'num_demo_participants': 1,
        'app_sequence': ['willingness_to_act'],
    },
{
        'name': 'self_assessment',
        'display_name': "Self-Assessment Questions",
        'num_demo_participants': 1,
        'app_sequence': ['self_assessment'],
    },
    {
        'name': 'icl',
        'display_name': "Risk Aversion - Staircase Method",
        'num_demo_participants': 1,
        'app_sequence': ['icl'],
    },
    {
        'name': 'mpl',
        'display_name': "Risk Aversion - Multiple Price List",
        'num_demo_participants': 1,
        'app_sequence': ['mpl'],
    },
    {
        'name': 'icl_time',
        'display_name': "Patience (Today vs. 12 Months) - Staircase Method",
        'num_demo_participants': 1,
        'app_sequence': ['icl_time'],
    },
    {
        'name': 'icl_time_2',
        'display_name': "Patience (12 Months vs. 24 Months) - Staircase Method",
        'num_demo_participants': 1,
        'app_sequence': ['icl_time_2'],
    },
    {
        'name': 'reciprocity_hypothetical',
        'display_name': "Positive Reciprocity Hypothetical Question",
        'num_demo_participants': 1,
        'app_sequence': ['reciprocity_hypothetical'],
    },
    {
        'name': 'altruism_hypothetical',
        'display_name': "Altruism Hypothetical Question",
        'num_demo_participants': 1,
        'app_sequence': ['altruism_hypothetical'],
    },
]


# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '$89h(ho1ce&^#rqd$vt+us($26)$-6&e)l*86u_rb@wwb)l39p'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
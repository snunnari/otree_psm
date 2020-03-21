from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'reciprocity_hypothetical'
    players_per_group = None
    num_rounds = 1

    stranger_cost = 20
    cheap_present = 5
    expensive_present = 30


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    reciprocity_hypothetical = models.StringField(
        choices=['No present', 'The present worth 5 Euro', 'The present worth 10 Euro',
                 'The present worth 15 Euro', 'The present worth 20 Euro',
                 'The present worth 25 Euro', 'The present worth 30 Euro'],
        widget=widgets.RadioSelect,
        label=''
    )

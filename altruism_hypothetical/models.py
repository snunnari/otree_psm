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
    name_in_url = 'altruism_hypothetical'
    players_per_group = None
    num_rounds = 1

    endowment = 1000


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    altruism_hypothetical = models.IntegerField(
        min=0, max=Constants.endowment,
        label=''
    )


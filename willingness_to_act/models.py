from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'willingness_to_act'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    altruism_qual = models.StringField(
        choices=['0 - Per niente disposto a farlo', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                 '10 - Completamente disposto a farlo'],
        label='',
        widget=widgets.RadioSelect)



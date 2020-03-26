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
    name_in_url = 'negative_reciprocity'
    players_per_group = None
    num_rounds = 1

    # prize from the lottery
    endowment = 100


class Subsession(BaseSubsession):

    def creating_session(self):
        # create Part index to show in templates' title (i.e., "Part <index>")
        # ---------------------------------------------------------------------------------------------------------
        if "p.participant.vars['part_index']" not in globals():
            for p in self.get_players():
                p.participant.vars['part_index'] = 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    negative_reciprocity = models.IntegerField(
        label='',
        min=0, max=Constants.endowment
    )

    # create function to increase part index by 1 when App changes
    # ------------------------------------------------------------------------------------------------------------------
    def update_part_index(self):
        self.participant.vars['part_index'] = self.participant.vars['part_index'] + 1
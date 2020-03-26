from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'willingness_to_act'
    players_per_group = None
    num_rounds = 1

    # Levels of scale for willingness to act
    levels = [str(j) for j in range(10 + 1)]


class Subsession(BaseSubsession):

    def creating_session(self):

        # create Part index to show in templates' title (i.e., "Part <index>")
        # --------------------------------------------------------------------------------------------------------------
        if "p.participant.vars['part_index']" not in globals():
            for p in self.get_players():
                p.participant.vars['part_index'] = 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    forego_future = models.StringField(
        choices=[
            ['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''],
            ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']
        ],
        label="""
        How willing are you to give up something that is beneficial for you today 
        in order to benefit more from that in the future?
        """,
        widget=widgets.RadioSelect)

    punish_unfair = models.StringField(
        choices=[
            ['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''],
            ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']
        ],
        label="""
        How willing are you to punish someone who treats you unfairly, 
        even if there may be costs for you? 
        """,
        widget=widgets.RadioSelect)

    punish_unfair_others = models.StringField(
        choices=[
            ['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''],
            ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']
        ],
        label="""
        How willing are you to punish someone who treats others unfairly, 
        even if there may be costs for you? 
        """,
        widget=widgets.RadioSelect)

    give_free = models.StringField(
        choices=[
            ['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''],
            ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']
        ],
        label="""
        How willing are you to give to good causes without expecting anything in return?
        """,
        widget=widgets.RadioSelect)

    # create function to increase part index by 1 when App changes
    # ------------------------------------------------------------------------------------------------------------------
    def update_part_index(self):
        self.participant.vars['part_index'] = self.participant.vars['part_index'] + 1

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


class Constants(BaseConstants):
    name_in_url = 'self_assessment'
    players_per_group = None
    num_rounds = 1

    # Levels of scale for self-assessment
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

    favor_return = models.StringField(
            choices=[
                ['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''],
                ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']
            ],
            label="""
            When someone does me a favor I am willing to return it. 
            """,
            widget=widgets.RadioSelect)

    unjust_revenge = models.StringField(
            choices=[
                ['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''],
                ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']
            ],
            label="""
            If I am treated very unjustly, I will take revenge at the first occasion, 
            even if there is a cost to do so.  
            """,
            widget=widgets.RadioSelect)

    people_best_intent = models.StringField(
            choices=[
                ['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''],
                ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']
            ],
            label="""
            I assume that people have only the best intentions. 
            """,
            widget=widgets.RadioSelect)

    risk_assessment = models.StringField(
            choices=[
                ['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''],
                ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']
            ],
            label="""
            In general, how willing or unwilling are you to take risks?
            """,
            widget=widgets.RadioSelect)

    # create function to increase part index by 1 when App changes
    # ------------------------------------------------------------------------------------------------------------------
    def update_part_index(self):
        self.participant.vars['part_index'] = self.participant.vars['part_index'] + 1
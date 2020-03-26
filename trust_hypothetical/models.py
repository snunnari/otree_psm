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
    name_in_url = 'trust_hypothetical'
    players_per_group = None
    num_rounds = 1

    # instructions template across pages
    instructions_template = 'trust_hypothetical/Instructions.html'

    # endowment, multiplication rate, amount transferred by the counterpart
    # ------------------------------------------------------------------------------------------------------------------
    endowment = 20
    rate = 3
    other_transfer = 5
    currency = '€'
    max_endowment = (rate + 1) * endowment  # only for instructions


class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.participant.vars['other_transfer'] = Constants.other_transfer
            p.participant.vars['final_endowment'] = Constants.endowment

            # dynamic form fields
            p.participant.vars['form_fields'] = [['transfer1'], ['transfer2'], ['transfer3'], ['transfer4']]

            # create Part index to show in templates' title (i.e., "Part <index>")
            # ----------------------------------------------------------------------------------------------------------
            if "p.participant.vars['part_index']" not in globals():
                p.participant.vars['part_index'] = 1


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # fields for the amount the player transfers at each of the five questions
    # ------------------------------------------------------------------------------------------------------------------
    transfer1 = models.IntegerField(
        min=0,
        label=''
    )

    transfer2 = models.IntegerField(
        min=0,
        label=''
    )

    transfer3 = models.IntegerField(
        min=0,
        label=''
    )

    transfer4 = models.IntegerField(
        min=0,
        label=''
    )

    transfer5 = models.IntegerField(
        min=0, max=Constants.endowment,
        label=''
    )

    # create function to determine maximum amount the participant can transfer at each of the four questions
    # ------------------------------------------------------------------------------------------------------------------
    def transfer1_max(self):
        return self.participant.vars['final_endowment']

    def transfer2_max(self):
        return self.participant.vars['final_endowment']

    def transfer3_max(self):
        return self.participant.vars['final_endowment']

    def transfer4_max(self):
        return self.participant.vars['final_endowment']

    # create function to increase transfer by 5 at each question
    # ------------------------------------------------------------------------------------------------------------------
    def increase_other_transfer(self):
        self.participant.vars['other_transfer'] += 5

    # create function to compute the players' endowment at each turn
    # ------------------------------------------------------------------------------------------------------------------
    def compute_endowment(self):
        self.participant.vars['final_endowment'] = Constants.endowment + Constants.rate \
                                                   * self.participant.vars['other_transfer']
        self.participant.vars['other_endowment'] = Constants.endowment - self.participant.vars['other_transfer']

    # create function to increase part index by 1 when App changes
    # ------------------------------------------------------------------------------------------------------------------
    def update_part_index(self):
        self.participant.vars['part_index'] = self.participant.vars['part_index'] + 1

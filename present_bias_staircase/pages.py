from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


# variables for all templates
# --------------------------------------------------------------------------------------------------------------------
def vars_for_all_templates(self):
    return {
        # 'p_hi': "{0:.1f}".format(Constants.probability) + "%",
        # 'p_lo': "{0:.1f}".format(100 - Constants.probability) + "%",
        'p_hi': "{0:.0f}".format(Constants.probability) + "%",
        'p_lo': "{0:.0f}".format(100 - Constants.probability) + "%",
        'hi':   "{0:.0f}".format(Constants.lottery_hi),
        'lo':   "{0:.0f}".format(Constants.lottery_lo),
        'part_index': self.participant.vars['part_index']
    }


# ******************************************************************************************************************** #
# *** CLASS INSTRUCTIONS *** #
# ******************************************************************************************************************** #
class Instructions(Page):

    # only display instruction in round 1
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        return self.subsession.round_number == 1

    def vars_for_template(self):
        return dict(
            in_12_months=Constants.in_12_months,
            in_24_months=Constants.in_24_months
        )


# ******************************************************************************************************************** #
# *** PAGE DECISION *** #
# ******************************************************************************************************************** #
class Decision(Page):

    # only display if previous choice was not "indifferent"
    # ----------------------------------------------------------------------------------------------------------------
    def is_displayed(self):
        previous_choices = [p.choice for p in self.player.in_previous_rounds()]
        return 'I' not in previous_choices

    # form model and form fields
    # ----------------------------------------------------------------------------------------------------------------
    form_model = 'player'
    form_fields = ['choice']

    # variables for template
    # ----------------------------------------------------------------------------------------------------------------
    def vars_for_template(self):

        # specify info for progress bar
        total = Constants.num_choices
        page = self.subsession.round_number
        progress = page / total * 100

        return {
            'page':        page,
            'total':       total,
            'progress':    progress,
            'sure_payoff': "{0:.0f}".format(self.participant.vars['icl_sure_payoffs'][page - 1])
        }

    # set sure payoffs for next choice, payoffs, and switching row
    # ----------------------------------------------------------------------------------------------------------------
    def before_next_page(self):
        self.player.set_sure_payoffs()
        self.player.update_switching_row()
        self.player.set_final_switching_row()
        if self.subsession.round_number == Constants.num_choices:
            self.player.update_part_index()


# ******************************************************************************************************************** #
# *** PAGE SEQUENCE *** #
# ******************************************************************************************************************** #
page_sequence = [Decision]

if Constants.instructions:
    page_sequence.insert(0, Instructions)

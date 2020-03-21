from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Altruism(Page):
    form_model = 'player'
    form_fields = ['altruism_hypothetical']

    def vars_for_template(self):
        return dict(
            endowment=Constants.endowment
        )


page_sequence = [Altruism]

from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Reciprocity(Page):
    form_model = 'player'
    form_fields = ['reciprocity_hypothetical']

    def vars_for_template(self):
        return dict(
            stranger_cost=Constants.stranger_cost,
            cheap_present=Constants.cheap_present,
            expensive_present=Constants.expensive_present
        )


class Results(Page):
    pass


page_sequence = [Reciprocity]

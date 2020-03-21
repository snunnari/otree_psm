from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class WillingnessToAct(Page):
    form_model = 'player'
    form_fields = ['forego_future', 'punish_unfair', 'punish_unfair_others', 'give_free']

    def vars_for_template(self):
        return dict(
            levels=Constants.levels,
        )


page_sequence = [
    WillingnessToAct,
]
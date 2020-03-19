from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class WillingnessToAct(Page):
    form_model = 'player'
    form_fields = ['forego_future', 'punish_unfair', 'punish_unfair_others', 'give_free']

    def vars_for_template(self):
        return dict(
            willingness_scale=Constants.willingness_scale,
            levels=Constants.levels,
            interval=Constants.interval,
        )


page_sequence = [
    WillingnessToAct,
]

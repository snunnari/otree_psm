from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class SelfAssessment(Page):
    form_model = 'player'
    form_fields = ['favor_return', 'unjust_revenge', 'people_best_intent']

    def vars_for_template(self):
        return dict(
            levels=Constants.levels,
        )


class RiskAssessment(Page):
    form_model = 'player'
    form_fields = ['risk_assessment']

    def vars_for_template(self):
        return dict(
            levels=Constants.levels,
        )


page_sequence = [
    SelfAssessment,
    RiskAssessment
]

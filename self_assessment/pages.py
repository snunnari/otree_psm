from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class RiskQualitative(Page):
    form_model = 'player'
    form_fields = ['risk_qual']


page_sequence = [
    RiskQualitative
]

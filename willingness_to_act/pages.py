from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class AltruismQualitative(Page):
    form_model = 'player'
    form_fields = ['altruism_qual']

page_sequence = [
    AltruismQualitative,
]

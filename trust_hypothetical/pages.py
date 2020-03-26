from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


def vars_for_all_templates(self):
    return dict(
        endowment=Constants.endowment,
        rate=Constants.rate,
        max_endowment=Constants.max_endowment,
        other_transfer=Constants.other_transfer,
        page=self.subsession.round_number,
        part_index=self.participant.vars['part_index'],
        currency=Constants.currency,
        instructions=Constants.instructions_template
    )


class Instructions(Page):
    pass


class Introduction(Page):

    form_model = 'player'

    def before_next_page(self):
        return self.player.compute_endowment()


class Question1(Page):

    form_model = 'player'
    form_fields = ['transfer1']

    def vars_for_template(self):
        return dict(
            other_endowment=self.participant.vars['other_endowment'],
            final_endowment=self.participant.vars['final_endowment'],
            other_transfer=self.participant.vars['other_transfer']
        )

    def before_next_page(self):
        print(self.subsession.round_number)
        return self.player.increase_other_transfer(), self.player.compute_endowment()


class Question2(Page):

    form_model = 'player'
    form_fields = ['transfer2']

    def vars_for_template(self):
        return dict(
            other_endowment=self.participant.vars['other_endowment'],
            final_endowment=self.participant.vars['final_endowment'],
            other_transfer=self.participant.vars['other_transfer']
        )

    def before_next_page(self):
        return self.player.increase_other_transfer(), self.player.compute_endowment()


class Question3(Page):

    form_model = 'player'
    form_fields = ['transfer3']

    def vars_for_template(self):
        return dict(
            other_endowment=self.participant.vars['other_endowment'],
            final_endowment=self.participant.vars['final_endowment'],
            other_transfer=self.participant.vars['other_transfer']
        )

    def before_next_page(self):
        return self.player.increase_other_transfer(), self.player.compute_endowment()


class Question4(Page):

    form_model = 'player'
    form_fields = ['transfer4']

    def vars_for_template(self):
        return dict(
            other_endowment=self.participant.vars['other_endowment'],
            final_endowment=self.participant.vars['final_endowment'],
            other_transfer=self.participant.vars['other_transfer'],
        )

    def before_next_page(self):
        return self.player.increase_other_transfer(), self.player.compute_endowment(),


class Question5(Page):

    form_model = 'player'
    form_fields = ['transfer5']

    def before_next_page(self):
        return self.player.update_part_index()


page_sequence = [Introduction,
                 Question1, Question2, Question3, Question4,
                 Question5]

#page_sequence.append(Question5)

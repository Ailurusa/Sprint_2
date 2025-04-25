class Results:
    team_type = ''
    modifier = 0

    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

    def number_of_wins(self):
        return f'{self.team_type} побед: {self.victories}'

    def number_of_draws(self):
        return f'{self.team_type} ничьих: {self.draws}'

    def number_of_losses(self):
        return f'{self.team_type} поражений: {self.losses}'

    def total_points(self):
        return f'Общее количество очков: {self.modifier * self.victories + self.draws}'


class Football(Results):
    team_type = 'Футбольных'
    modifier = 3


class Hockey(Results):
    team_type = 'Хоккейных'
    modifier = 2


football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in (football_team, hockey_team):
    team.number_of_wins()
    team.number_of_draws()
    team.number_of_losses()
    team.total_points()

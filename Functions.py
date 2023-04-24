import seaborn as sns
import matplotlib.pyplot as plt

sns.set(font_scale=0.7)

teams_colors = {
    'Manchester United': '#DA291C',
    'Manchester City': '#6CABDD',
    'Chelsea': '#034694',
    'Arsenal': '#EF0107',
    'Liverpool': '#C8102E',
    'Leicester City': '#003090',
    'West Bromwich Albion': '#122F67',
    'Sunderland': '#eb172b',
    'Tottenham Hotspur ': '#132257',
    'Birmingham City': '#202959',
    'Derby County': '#231f20',
    'Norwich City': '#00A650',
    'Cardiff City': '#0070B5',
    'Fulham': '#000000',
    'Hull City': '#f5971d',
    'Queens Park Rangers': '#1d5ba4',
    'Newcastle United': '#241F20',
    'Aston Villa': '#670E36',
    'Everton': '#003399',
    'Middlesbrough': '#e11b22',
    'West Ham United': '#7A263A',
    'Stoke City': '#E03A3E',
    'Bolton Wanderers': '#263c7e'
}


def get_colors(clubs):
    return [teams_colors[key] for key in clubs]


def draw_pie_chart(labels, values, title):
    fig, ax = plt.subplots()
    _, _, autotexts = ax.pie(values, labels=labels, colors=get_colors(labels), autopct=lambda p: f'{p*sum(values)/100 :.0f} Titles')
    for autotext in autotexts:
        autotext.set_color('white')
    plt.title(title)
    plt.show()
    # plt.subplots() is a function that returns a tuple containing a figure and axes object(s).
    # Thus when using fig, ax = plt.subplots() you unpack this tuple into the variables fig and ax.


def draw_barplot(x, y, palette, title, x_label, y_label):
    sns.barplot(x=x, y=y, palette=palette)
    for index, data in enumerate(y):
        plt.text(x=index, y=data+0.1, s="%.0f" % data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()


def draw_lineplot(seasons, points, color, title):
    sns.lineplot(x=seasons, y=points, color=color[0])
    for index, data in enumerate(points):
        plt.text(x=index + 0.1, y=data, s="%.0f" % data)
    plt.title(title)
    plt.xlabel('Seasons')
    plt.ylabel('Points')
    plt.ylim(0, 100)
    plt.show()


def winning_clubs(data, title):
    winners = data.team[data.position == 1].value_counts()
    draw_pie_chart(labels=winners.index, values=winners, title=title)


def champions_league_clubs(data, title):
    champions = data.team[data.position <= 4].value_counts().head(5)
    draw_barplot(x=champions.index, y=champions, palette=get_colors(champions.index), title=title, x_label='Teams', y_label='Qualification')


def worst_clubs(data, title):
    losers = data.team[data.position >= 18].value_counts().head(5)
    draw_barplot(x=losers.index, y=losers, palette=get_colors(losers.index), title=title, x_label='Teams', y_label='Relegation')


def most_in(data, series, title):
    teams = data.groupby('team')[[series]].sum().sort_values(series, ascending=False).head(5)
    draw_barplot(x=teams.index, y=getattr(teams, series), palette=get_colors(teams.index), title=title, x_label='Teams', y_label=series)


def team_performance(data, team, title):
    seasons = data.season.unique()[::-1].tolist()
    seasons_dictionary = {season: 0 for season in seasons}
    for key, value in seasons_dictionary.items():
        try:
            seasons_dictionary[key] = data.points[(data.team == team) & (data.season == key)].values.tolist()[0]
        except IndexError:
            seasons_dictionary[key] = 0
    draw_lineplot(seasons=seasons, points=seasons_dictionary.values(), color=get_colors([team]), title=title)




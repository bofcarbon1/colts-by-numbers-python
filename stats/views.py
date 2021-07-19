from django.http import HttpResponse
from django.shortcuts import render
from statistics import mean
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import matplotlib
matplotlib.use('Agg')


# def do_nfl():
#    games = nflgame.games(2019, week=2, away='IND')
#    players = nflgame.combine_game_stats(games)
#    rushers = players.rushing().sort('rushing_yds')  # .limit(5)
#    colts = []
#    colts2 = []
#    for rusher in rushers:
#        colts.append(rusher)
#    for colt in colts:
#        if str(colt).__contains__('Mack') \
#               or str(colt).__contains__('Hines') \
#               or str(colt).__contains__('Wilkins') \
#               or str(colt).__contains__('Williams') \
#               or str(colt).__contains__('Brissett'):
#            colts2.append(colt)

#    return colts2


def index(request):
    img_name = '/media/cwentz.jpeg'
    return render(request, 'index.html', {'cWentz_image_url': img_name})


def do_graph():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [203, 167, 79, 81, 180, 62, 127, 139, 109, 264, 175, 82, 66, 46, 218, 132])  # Plot some data on the axes.

    plt.title('2019 Rushing Yards')
    plt.ylabel('Total Yds')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    total_yds = [203, 167, 79, 81, 180, 62, 127, 139, 109, 264, 175, 82, 66, 46, 218, 132]
    avg = round(mean(total_yds), 0)
    plt.text(2, 250, r'avg yards=%a'%avg)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_off_run_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_off_run_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_team_pass_yds_graph():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [173, 121, 300, 265, 151, 321, 191, 189, 191, 125, 121, 309, 243, 159, 106, 143])  # Plot some data on the axes.

    plt.title('2019 Passing Yards')
    plt.ylabel('Total Yds')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    all_yds = [173, 121, 300, 265, 151, 321, 191, 189, 191, 125, 121, 309, 243, 159, 106, 143]
    # avg = sum(all_yds) / len(all_yds)
    # m_avg = round(avg, 0)
    avg = round(mean(all_yds), 0)
    plt.text(2, 250, r'avg yards=%a'%avg)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_off_pass_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_off_pass_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_team_first_downs_graph():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [22, 21, 29, 22, 25, 23, 19, 22, 19, 23, 19, 22, 16, 16, 25, 17])  # Plot some data on the axes.

    plt.title('2019 1st Downs')
    plt.ylabel('1st Downs')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    all_yds = [22, 21, 29, 22, 25, 23, 19, 22, 19, 23, 19, 22, 16, 16, 25, 17]
    avg = round(mean(all_yds), 0)
    plt.text(2, 250, r'avg firsts=%a'%avg)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_off_fdowns_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_off_fdowns_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_team_div_pass_rating_bar():
    style.use('ggplot')

    labels = ['Titans', 'Colts', 'Texans']
    prd_2019 = [107.9, 85, 96.5]
    prd_2020 = [98, 95, 94]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, prd_2019, width, label='2019 Actual', color=(0.2, 0.4, 0.6, 0.6))
    rects2 = ax.bar(x + width / 2, prd_2020, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Pass Rating')
    ax.set_xlabel('Team')
    ax.set_title('AFC South Passer Ratings')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/team_off_div_passrtngs_bar_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_off_div_passrtngs_bar_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_team_div_rush_yds_bar():
    style.use('ggplot')

    labels = ['Titans', 'Colts', 'Texans']
    ryd_2019 = [2223, 2130, 2009]
    ryd_2020 = [2200, 2200, 2000]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, ryd_2019, width, label='2019 Actual', color=(0.2, 0.4, 0.6, 0.6))
    rects2 = ax.bar(x + width / 2, ryd_2020, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Rush Yards')
    ax.set_xlabel('Team')
    ax.set_title('AFC South Rushing Yards')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/team_off_div_rushyds_bar_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_off_div_rushyds_bar_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def stats_factory(request):
    # nfl_data = do_nfl()
    # return render(request, 'factory.html', {'nfl_data': nfl_data})
    return render(request, 'factory.html')

def team_offense(request):
    # img_name = do_graph()
    # img_name = do_team_pass_yds_graph()
    # img_name = do_team_first_downs_graph()
    img_name = do_team_div_pass_rating_bar()
    img_name = do_team_div_rush_yds_bar()
    # return render(request, 'team_offense.html', {'team_off_run_stats_graph_img': img_name})
    # return render(request, 'team_offense.html', {'team_off_pass_stats_graph_img': img_name})
    # return render(request, 'team_offense.html', {'team_off_fdowns_stats_graph_img': img_name})
    # return render(request, 'team_offense.html', {'team_off_div_passrtngs_bar_img': img_name})
    return render(request, 'team_offense.html', {'team_off_div_rushyds_bar_img': img_name})


def do_player_offense_runs_graph():
    style.use('ggplot')

    labels = ['Mack', 'Taylor', 'Wilkins', 'Hines']
    runs_2019 = [1091, 0, 307, 199]
    runs_2020 = [1025, 575, 270, 235]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, runs_2019, width, label='2019 Actual', color=(0.2, 0.4, 0.6, 0.6))
    rects2 = ax.bar(x + width / 2, runs_2020, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Yards')
    ax.set_xlabel('Player')
    ax.set_title('Colts Top Rushers')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/player_off_runs_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/player_off_runs_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_player_offense_rec_graph():
    style.use('ggplot')

    labels = ['Pascal', 'Hilton', 'Doyle', 'Pittman']
    rec_2019 = [607, 501, 448, 0]
    rec_2020 = [475, 625, 605, 425]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, rec_2019, width, label='2019 Actual', color=(0.2, 0.4, 0.6, 0.6))
    rects2 = ax.bar(x + width / 2, rec_2020, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Yards')
    ax.set_xlabel('Player')
    ax.set_title('Colts Top Receivers')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/player_off_recs_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/player_off_recs_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_rivers_pass_yds_graph():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [333, 293, 318, 310, 211, 320, 329, 201, 294, 207, 353, 265, 314, 307, 279, 281])  # Plot some data on the axes.

    plt.title('2019 Rivers Passing Yards')
    plt.ylabel('Total Yds')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    all_yds = [333, 293, 318, 310, 211, 320, 329, 201, 294, 207, 353, 265, 314, 307, 279, 281]
    avg = round(mean(all_yds), 0)
    plt.text(3, 340, r'avg yards=%a'%avg)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/rivers_2019_pass_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/rivers_2019_pass_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_rivers_pass_rating_graph():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [121.3, 73, 101.5, 131.9, 58.6, 77.8, 108.3, 82.7, 108.3, 57.5, 49.6, 106.3, 154.4, 71.2, 89.6, 80.1])  # Plot some data on the axes.

    plt.title('2019 Rivers Passer Rating')
    plt.ylabel('Pass Rating')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    all_rts = [121.3, 73, 101.5, 131.9, 58.6, 77.8, 108.3, 82.7, 108.3, 57.5, 49.6, 106.3, 154.4, 71.2, 89.6, 80.1]
    avg = round(mean(all_rts), 0)
    plt.text(5, 140, r'avg rating=%a'%avg)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/rivers_2019_pass_ratings_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/rivers_2019_pass_ratings_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_rivers_qbr_graph():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [50.9, 52.3, 46.4, 77.1, 31.6, 20.6, 80.7, 38.7, 68.8, 25.2, 25.8, 48.3, 84.5, 55.5, 38.4, 53.9])  # Plot some data on the axes.

    plt.title('2019 Rivers QBR')
    plt.ylabel('QBR')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    all_qbr =  [50.9, 52.3, 46.4, 77.1, 31.6, 20.6, 80.7, 38.7, 68.8, 25.2, 25.8, 48.3, 84.5, 55.5, 38.4, 53.9]
    avg = round(mean(all_qbr), 0)
    plt.text(8, 80, r'avg QBR=%a'%avg)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/rivers_2019_qbr_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/rivers_2019_qbr_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def player_offense(request):
    img_name = do_player_offense_runs_graph()
    # img_name = do_player_offense_rec_graph()
    # img_name = do_team_first_downs_graph()
    # img_name = do_rivers_pass_yds_graph()
    # img_name = do_rivers_pass_rating_graph()
    # img_name = do_rivers_qbr_graph()
    return render(request, 'player_offense.html', {'player_off_runs_stats_graph_img': img_name})
    # return render(request, 'player_offense.html', {'player_off_recs_stats_graph_img': img_name})
    # return render(request, 'player_offense.html', {'rivers_2019_pass_stats_graph_img': img_name})
    # return render(request, 'player_offense.html', {'rivers_2019_pass_ratings_graph_img': img_name})
    # return render(request, 'player_offense.html', {'rivers_2019_qbr_stats_graph_img': img_name})

    # return render(request, 'player_offense.html', {'player_off_fdowns_stats_graph_img': img_name})


def do_team_defense_run_yds_graph():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [125, 124, 93, 188, 36, 100, 113, 90, 70, 29, 99, 154, 75, 117, 87, 67])  # Plot some data on the axes.

    plt.title('2019 Rushing Yards Allowed')
    plt.ylabel('Total Yds')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    total_yds = [125, 124, 93, 188, 36, 100, 113, 90, 70, 29, 99, 154, 75, 117, 87, 67]
    avg = round(mean(total_yds), 0)
    plt.text(6, 170, r'avg yards=%a'%avg)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_def_run_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_def_run_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_team_defense_pass_yds_graph():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [310, 119, 304, 189, 288, 291, 166, 183, 159, 279, 297, 138, 467, 307, 199, 286])  # Plot some data on the axes.

    plt.title('2019 Passing Yards Allowed')
    plt.ylabel('Total Yds')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    all_yds = [310, 119, 304, 189, 288, 291, 166, 183, 159, 279, 297, 138, 467, 307, 199, 286]
    # avg = sum(all_yds) / len(all_yds)
    # m_avg = round(avg, 0)
    avg = round(mean(all_yds), 0)
    plt.text(3, 400, r'avg yards=%a'%avg)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_def_pass_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_def_pass_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_team_defense_first_downs_graph():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
            [25, 18, 25, 21, 18, 21, 21, 17, 13, 15, 16, 15, 29, 27, 19, 23])  # Plot some data on the axes.

    plt.title('2019 1st Downs Allowed')
    plt.ylabel('1st Downs')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    first_downs = [25, 18, 25, 21, 18, 21, 21, 17, 13, 15, 16, 15, 29, 27, 19, 23]
    avg = round(mean(first_downs), 0)
    plt.text(7, 27, r'avg firsts=%a'%avg)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_def_fdowns_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_def_fdowns_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_player_defense_sacks_graph():
    style.use('ggplot')

    labels = ['Houston', 'Buckner', 'Leonard', 'Moore']
    sacks_2019 = [11, 7.5, 5, 3]
    sacks_2020 = [12, 9, 6, 4]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, sacks_2019, width, label='2019 Actual', color=(0.2, 0.4, 0.6, 0.6))
    rects2 = ax.bar(x + width / 2, sacks_2020, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Sacks')
    ax.set_xlabel('Player')
    ax.set_title('Colts Top Sackers')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/player_def_sacks_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/player_def_sacks_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_player_defense_tackles_graph():
    style.use('ggplot')

    labels = ['Walker', 'Leonard', 'Willis', 'Okereke']
    sacks_2019 = [124, 121, 71, 65]
    sacks_2020 = [126, 123, 73, 67]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, sacks_2019, width, label='2019 Actual', color=(0.2, 0.4, 0.6, 0.6))
    rects2 = ax.bar(x + width / 2, sacks_2020, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Tackles')
    ax.set_xlabel('Player')
    ax.set_title('Colts Top Tacklers')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/player_def_tackles_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/player_def_tackles_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_player_defense_ints_graph():
    style.use('ggplot')

    labels = ['Leonard', 'Moore', 'Hooker', 'Ya-Sin']
    sacks_2019 = [5, 2, 2, 1]
    sacks_2020 = [6, 3, 3, 2]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, sacks_2019, width, label='2019 Actual', color=(0.2, 0.4, 0.6, 0.6))
    rects2 = ax.bar(x + width / 2, sacks_2020, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Interceptions')
    ax.set_xlabel('Player')
    ax.set_title('Colts Top Interceptors')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/player_def_ints_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/player_def_ints_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def team_defense(request):
    # img_name = do_team_defense_run_yds_graph()
    # img_name = do_team_defense_pass_yds_graph()
    img_name = do_team_defense_first_downs_graph()
    # return render(request, 'team_defense.html', {'team_def_run_stats_graph_img': img_name})
    # return render(request, 'team_defense.html', {'team_def_pass_stats_graph_img': img_name})
    return render(request, 'team_defense.html', {'team_def_fdowns_stats_graph_img': img_name})


def player_defense(request):
    # img_name = do_player_defense_sacks_graph()
    # return render(request, 'player_defense.html', {'player_def_sacks_stats_graph_img': img_name})
    # img_name = do_player_defense_tackles_graph()
    # return render(request, 'player_defense.html', {'player_def_tackles_stats_graph_img': img_name})
    img_name = do_player_defense_ints_graph()
    return render(request, 'player_defense.html', {'player_def_ints_stats_graph_img': img_name})
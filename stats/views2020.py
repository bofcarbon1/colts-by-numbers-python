import matplotlib
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from matplotlib import pyplot as plt
from matplotlib import style

matplotlib.use('Agg')


# This process uses BeautifulSoup from facebook to parse data
# Our site is Pro Football Reference specifically stats from games


# Remove the columns from
def rem_df_cols(arg_col_array, df_bs):
    # print("Started remove-df-columns using " + str(arg_col_array))
    for col in arg_col_array:
        del df_bs[col]


def make_beautiful_soup():
    product_url = "https://www.pro-football-reference.com/teams/clt/2020.htm"
    headers = {'user-agent': 'Mozilla/5.0'}  # to make the server think its a web browser and not a bot
    res = requests.get(product_url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    # print(soup.title)

    # Parse your soup, extract and build a dataframe
    table = soup.find(id='games')
    rows = table.find_all('tr')
    row_list = list()
    # print(row_list)
    for tr in rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        row_list.append(row)
        # print(row_list)
    df_bs = pd.DataFrame(row_list, columns=['Week', 'Day', 'Time', 'box', 'W',
                                       'OT', 'REC', '@', 'Team', 'Tm', 'Opp', 'O1stD', 'OTotYds', 'OPassY',
                                       'ORushY', 'OTO', 'D1stD', 'DTotYds', 'DPassY', 'DRushY', 'DTO', 'EPOff',
                                       'EPDef', 'EPs'])

    # Clean up the data for later use with MatplotLib
    rem_df_col_array = ['Week', 'Time', 'box', 'Day', 'W', 'OT', 'REC', '@', 'EPOff', 'EPDef', 'EPs']
    rem_df_cols(rem_df_col_array, df_bs)


def do_team_rush_yds_graph():
    style.use('ggplot')

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    y1 = [88, 151, 119, 103, 68, 59, 119, 112, 133, 140, 56, 109, 212, 127, 127, 273]
    ax.plot(x1, y1,  color='royalblue')
    x2 = [16]
    y2 = [273]
    ax.plot(x2, y2,  color='royalblue', linestyle='--')

    plt.legend(['Actual', 'Projected'], loc='upper right')
    plt.title('2020 Rushing Yards')
    plt.ylabel('Total Yds')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    avgory = round((88 + 151 + 119 + 103 + 68 + 59 + 119 + 112
                    + 133 + 140 + 56 + 109 + 212 + 127 + 127 + 273) / 16)
    plt.text(12, 90, r'avg yards=%a'%avgory)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_off_2020_run_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_off_2020_run_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    # ax2.clear()
    plt.close(fig)

    return img_name


def do_team_pass_yds_graph():
    style.use('ggplot')

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    y1 = [363, 214, 234, 186, 240, 371, 262, 227, 308, 288, 280, 262, 244, 223, 238, 164]
    ax.plot(x1, y1, color='royalblue')
    x2 = [16]
    y2 = [164]
    ax.plot(x2, y2, color='royalblue', linestyle='--')

    plt.legend(['Actual', 'Projected'], loc='upper right')
    plt.title('2020 Passing Yards')
    plt.ylabel('Total Yds')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    avg = round((363 + 214 + 234 + 186 + 240 + 371 + 262 + 227
                 + 308 + 288 + 280 + 262 + 244 + 223 + 238 + 164) / 16)
    plt.text(12, 300, r'avg yards=%a'%avg)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_off_2020_pass_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_off_2020_pass_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_team_first_downs_graph():
    style.use('ggplot')

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    y1 = [27, 24, 21, 18, 15, 23, 26, 20, 26, 23, 27, 25, 25, 20, 21, 23]
    ax.plot(x1, y1, color='royalblue')
    x2 = [16]
    y2 = [23]
    ax.plot(x2, y2, color='royalblue', linestyle='--')

    plt.legend(['Actual', 'Projected'], loc='upper right')
    plt.title('2020 1st Downs')
    plt.ylabel('1st Downs')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    avgofd = round((27 + 24 + 21 + 18 + 15 + 23 + 26 + 20 + 26
                    + 23 + 27 + 25 + 25 + 20 + 21 + 23) / 16)
    plt.text(12, 18, r'avg firsts=%a'%avgofd)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_off_2020_fdowns_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_off_2020_fdowns_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_team_div_pass_yds_bar():
    style.use('ggplot')

    labels = ['Texans', 'Colts',  'Jaguars',  'Titans']
    prd_2020 = [4819, 4186, 3924, 3814]
    prd_proj = [4819, 4186, 3924, 3814]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, prd_2020, width, label='2020 Actual', color=(0.2, 0.4, 0.6, 0.6))
    ax.bar(x + width / 2, prd_proj, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Pass Yards')
    ax.set_xlabel('Team')
    ax.set_title('AFC South Passing Yards')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/team_off_div_2020_pass_yds_bar_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_off_div_2020_pass_yds_bar_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_team_div_rush_yds_bar():
    style.use('ggplot')

    labels = ['Titans', 'Colts', 'Jaguars', 'Texans']
    ryd_2020 = [2690, 1996, 1519, 1466]
    ryd_proj = [2690, 1996, 1519, 1466]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, ryd_2020, width, label='2020 Actual', color=(0.2, 0.4, 0.6, 0.6))
    ax.bar(x + width / 2, ryd_proj, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Rush Yards')
    ax.set_xlabel('Team')
    ax.set_title('AFC South Rushing Yards')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/team_off_div_2020_rush_yds_bar_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_off_div_2020_rush_yds_bar_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def team_offense(request):
    print("Started team_offense")
    # img_name = do_team_rush_yds_graph()
    # img_name = do_team_pass_yds_graph()
    # img_name = do_team_first_downs_graph()
    # img_name = do_team_div_pass_yds_bar()
    # img_name = do_team_div_rush_yds_bar()
    # return render(request, 'team_offense_2020.html', {'team_off_2020_run_stats_graph_img': img_name})
    # return render(request, 'team_offense_2020.html', {'team_off_2020_pass_stats_graph_img': img_name})
    # return render(request, 'team_offense_2020.html', {'team_off_2020_fdowns_stats_graph_img': img_name})
    # return render(request, 'team_offense_2020.html', {'team_off_div_2020_pass_yds_bar_img': img_name})
    # return render(request, 'team_offense_2020.html', {'team_off_div_2020_rush_yds_bar_img': img_name})


def do_player_offense_runs_graph():
    style.use('ggplot')

    labels = ['Taylor', 'Hines', 'Wilkins']
    runs_2020 = [1169, 380, 308]
    runs_proj = [1169, 380, 308]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, runs_2020, width, label='2020 Actual', color=(0.2, 0.4, 0.6, 0.6))
    ax.bar(x + width / 2, runs_proj, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Yards')
    ax.set_xlabel('Player')
    ax.set_title('Colts Top Rushers')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/player_off_2020_runs_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/player_off_2020_runs_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_player_offense_rec_graph():
    style.use('ggplot')

    labels = ['Hilton', 'Pascal', 'Pittman', 'Hines']
    rec_2020 = [762, 629, 503, 482]
    rec_proj = [762, 629, 503, 482]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, rec_2020, width, label='2020 Actual', color=(0.2, 0.4, 0.6, 0.6))
    ax.bar(x + width / 2, rec_proj, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Yards')
    ax.set_xlabel('Player')
    ax.set_title('Colts Top Receivers')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/player_off_2020_recs_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/player_off_2020_recs_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_rivers_pass_rating_graph():
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    y1 = [88.7, 97.8, 125.6, 86.9, 89.4, 105.4,123.5, 62.8,
          105.5, 107.2, 84.9, 119.3, 118.7, 124.4, 84.2, 76.8]
    ax.plot(x1, y1, color='royalblue')
    x2 = [16]
    y2 = [84.2]
    ax.plot(x2, y2, color='royalblue', linestyle='--')
    plt.legend(['Actual', 'Projected'], loc='upper right')
    plt.title('2020 Rivers Passer Rating')
    plt.ylabel('Pass Rating')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    avgr = round((88.7 + 97.8 + 125.6 + 86.9 + 89.4 + 105.4
                  + 123.5 + 62.8 + 105.5 + 107.2 + 84.9 + 119.3
                  + 118.7 + 124.4 + 84.2 + 76.8) / 16)
    print("avgr: " + str(avgr))
    plt.text(12, 70, r'avg rating=%a'%avgr)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/rivers_2020_pass_ratings_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/rivers_2020_pass_ratings_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def player_offense(request):
    print("Started player_offense")
    # img_name = do_player_offense_runs_graph()
    # img_name = do_player_offense_rec_graph()
    # img_name = do_rivers_pass_rating_graph()
    # return render(request, 'player_offense_2020.html', {'player_off_2020_runs_stats_graph_img': img_name})
    # return render(request, 'player_offense_2020.html', {'player_off_2020_recs_stats_graph_img': img_name})
    # return render(request, 'player_offense_2020.html', {'rivers_2020_pass_ratings_graph_img': img_name})


def do_team_defense_run_yds_graph():
    style.use('ggplot')

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    y1 = [91, 80, 109, 28, 124, 98, 29, 110, 157, 66, 229, 90, 79, 83, 20, 53]
    ax.plot(x1, y1, color='royalblue')
    x2 = [16]
    y2 = [53]
    ax.plot(x2, y2, color='royalblue', linestyle='--')

    plt.legend(['Actual', 'Projected'], loc='upper right')
    plt.title('2020 Rushing Yards Allowed')
    plt.ylabel('Total Yds')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    avgdya = round((91 + 80 + 109 + 28 + 124 + 98 + 29 + 110
                    + 157 + 66 + 229 + 90 + 79 + 83 + 20 + 53) / 16)
    plt.text(12, 150, r'avg yards=%a'%avgdya)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_def_2020_run_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_def_2020_run_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_team_defense_pass_yds_graph():
    style.use('ggplot')

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    y1 = [150, 95, 151, 241, 261, 300, 297, 156, 137, 311, 220, 308, 345, 342, 333, 230]
    ax.plot(x1, y1, color='royalblue')
    x2 = [16]
    y2 = [230]
    ax.plot(x2, y2, color='royalblue', linestyle='--')

    plt.legend(['Actual', 'Projected'], loc='upper right')
    plt.title('2020 Passing Yards Allowed')
    plt.ylabel('Total Yds')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    avgpya = round((150 + 95 + 151 + 241 + 261 + 300 + 297 + 156 + 137
                    + 311 + 280 + 308 + 345 + 342 + 333 + 230) / 16)
    plt.text(10, 140, r'avg yards=%a'%avgpya)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_def_2020_pass_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_def_2020_pass_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_team_defense_first_downs_graph():
    style.use('ggplot')

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    y1 = [17, 12, 15, 16, 22, 22, 20, 19, 25, 21, 28, 20, 26, 22, 26, 18]
    ax.plot(x1, y1, color='royalblue')
    x2 = [16]
    y2 = [18]
    ax.plot(x2, y2, color='royalblue', linestyle='--')

    plt.legend(['Actual', 'Projected'], loc='upper right')
    plt.title('2020 1st Downs Allowed')
    plt.ylabel('1st Downs')
    plt.xlabel('Games')
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])

    avgdfd = round((17 + 12 + 15 + 16 + 22 + 22 + 20 + 19 + 25
                    + 21 + 28 + 20 + 26 + 22 + 26 + 18) / 16)
    plt.text(12, 16, r'avg firsts=%a'%avgdfd)
    plt.grid(True)

    ax.set_facecolor('#87CEFA')

    filename = './media/team_def_2020_fdowns_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/team_def_2020_fdowns_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_player_defense_sacks_graph():
    style.use('ggplot')

    labels = ['Buckner', 'Houston', 'Autry', 'Lewis']
    sacks_2020 = [9.5, 8, 7.5, 4]
    sacks_proj = [9.5, 8, 7.5, 4]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, sacks_2020, width, label='2020 Actual', color=(0.2, 0.4, 0.6, 0.6))
    ax.bar(x + width / 2, sacks_proj, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Sacks')
    ax.set_xlabel('Player')
    ax.set_title('Colts Top Sackers')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/player_def_2020_sacks_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/player_def_2020_sacks_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_player_defense_tackles_graph():
    style.use('ggplot')

    labels = ['Leonard', 'Walker', 'Willis', 'Moore']
    tackles_2020 = [132, 92, 85, 80]
    tackles_proj = [132, 92, 85, 80]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, tackles_2020, width, label='2020 Actual', color=(0.2, 0.4, 0.6, 0.6))
    ax.bar(x + width / 2, tackles_proj, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Tackles')
    ax.set_xlabel('Player')
    ax.set_title('Colts Top Tacklers')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/player_def_2020_tackles_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/player_def_2020_tackles_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def do_player_defense_ints_graph():
    style.use('ggplot')

    labels = ['Moore', 'Rhodes', 'Willis', 'Carrie']
    ints_2020 = [4, 2, 2, 2]
    ints_proj = [4, 2, 2, 2]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x - width / 2, ints_2020, width, label='2020 Actual', color=(0.2, 0.4, 0.6, 0.6))
    ax.bar(x + width / 2, ints_proj, width, label='2020 Projected', color='royalblue')

    # Add some text for labels, title and custom x - axis tick labels, etc.

    ax.set_ylabel('Interceptions')
    ax.set_xlabel('Player')
    ax.set_title('Colts Top Interceptors')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    filename = './media/player_def_2020_ints_stats_graph_img.svg'

    fig.savefig(filename)
    img_name = '/media/player_def_2020_ints_stats_graph_img.svg'

    # Cleanup Threads
    fig.clear()
    ax.clear()
    plt.close(fig)

    return img_name


def team_defense(request):
    print("Started team_defense")
    # img_name = do_team_defense_run_yds_graph()
    # img_name = do_team_defense_pass_yds_graph()
    img_name = do_team_defense_first_downs_graph()
    # return render(request, 'team_defense_2020.html', {'team_def_2020_run_stats_graph_img': img_name})
    # return render(request, 'team_defense_2020.html', {'team_def_2020_pass_stats_graph_img': img_name})
    return render(request, 'team_defense_2020.html', {'team_def_2020_fdowns_stats_graph_img': img_name})


def player_defense(request):
    print("Started player_defense")
    # img_name = do_player_defense_sacks_graph()
    # return render(request, 'player_defense_2020.html', {'player_def_2020_sacks_stats_graph_img': img_name})
    # img_name = do_player_defense_tackles_graph()
    # return render(request, 'player_defense_2020.html', {'player_def_2020_tackles_stats_graph_img': img_name})
    # img_name = do_player_defense_ints_graph()
    # return render(request, 'player_defense_2020.html', {'player_def_2020_ints_stats_graph_img': img_name})

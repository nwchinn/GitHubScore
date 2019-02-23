"""
Githubscore index (main) view.

URLs include:
/leaderboard
"""
import flask
import githubscore
import requests

from githubscore.model import get_db


# TO DO:
@githubscore.app.route('/leaderboard')
def show_leaderboard():
    """Display / route."""
    # username = 'nwchinn'
    # response = requests.get("https://api.github.com/users/" + username)
    # user_data = response.json()
    # print(user_data)
    # print('Name: ', user_data['name'])
    # print('login: ', user_data['login'])
    # print('Followers: ', user_data['followers'])
    # print('Following: ', user_data['following'])
    # print('Public Repos: ', user_data['public_repos'])


    context = {}

    db = get_db()
    cur = db.cursor()
    cur = cur.execute('''SELECT * FROM users WHERE login= "nwchinn"''').fetchone()
    # context = cur.fetchall()
    print('type: ', type(cur))
    # context['login'] = user_data['login']
    context['login'] = 'LEADERBOARD'
    return flask.render_template("leaderboard.html", **context)

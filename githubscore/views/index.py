"""
Githubscore index (main) view.

URLs include:
/
"""
import flask
import githubscore
import requests

from githubscore.model import get_db
from githubscore.views.helper import get_stars

# TO DO:
@githubscore.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Display / route."""
    
    context = {}
    db = get_db()

    if flask.request.method == 'POST':
        # Get results of users submissions
        form_in = flask.request.form.to_dict()
        # print('POST - req: ', req)
        # print('username: ', type(form_in['username']))

        # Pass entered username to context dic for HTML
        context['username_in'] = form_in['username']

        # Check how many times username appears in the DB
        select_if_in = "SELECT COUNT(*) FROM users where login = ?"
        results = get_db().cursor().execute(
                select_if_in, (form_in['username'],)).fetchone()

        # Check if username count = 1 (Present) or 0 (Not Present)
        if results['COUNT(*)'] == 0:
            print('Username is not in DB')

            # Grab username data from GitHub API
            response = requests.get("https://api.github.com/users/" + form_in['username'])
            print("api status code: ", response.status_code)
            user_data = response.json()
            print('user_data: ', user_data)

            #TODO: Check that username exists on github
            if response.status_code != 200:
                print('ERROR: Api failure')
            else:
                # print('user_data type: ', type(user_data))
                # print('Name: ', user_data['name'])
                # print('login: ', user_data['login'])
                # print('Followers: ', user_data['followers'])
                # print('Following: ', user_data['following'])
                # print('Public Repos: ', user_data['public_repos'])

                get_stars()

                insert_user = '''INSERT INTO users(login, gid, name, email, followers, following, public_repos, public_gists, repos_url) 
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
                get_db().cursor().execute(
                    insert_user, (user_data['login'], user_data['id'], user_data['name'],
                     user_data['email'], user_data['followers'], user_data['following'], 
                     user_data['public_repos'], user_data['public_gists'], user_data['public_repos'] ))

            context.update(user_data)

        else:
            print('Username is present')
            # Grab user data from DB
            select_user = "SELECT * FROM users where login = ?"
            results = get_db().cursor().execute(
            select_user, (form_in['username'],)).fetchone()
            # print(form_in['username'], ' Data(Results): ', results)
            # Add users information to context dic for HTML
            context.update(results)

            
            
    
    print('Context: ', context)
    # cur = db.cursor()
    # cur = cur.execute('''SELECT * FROM users WHERE login= "nwchinn"''').fetchone()
    # context = cur.fetchall()
    # print('type: ', type(cur))
    # context['login'] = user_data['login']
    # context['login'] = 'nwchinn'
    return flask.render_template("index.html", **context)





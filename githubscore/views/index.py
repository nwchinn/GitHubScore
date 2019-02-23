"""
Githubscore index (main) view.

URLs include:
/
"""
import flask
import githubscore
import requests

from githubscore.model import get_db

# TO DO:
@githubscore.app.route('/', methods=['GET', 'POST'])
def show_index():
    """Display / route."""
    
    context = {}
    db = get_db()

    if flask.request.method == 'POST':
    	# Get results of users submissions
    	req = flask.request.form.to_dict()
    	# print('POST - req: ', req)
    	# print('username: ', req['username'])
  		# Pass entered username to context dic for HTML
    	context['username_in'] = req['username']

    	# Check how many times username appears in the DB
    	cur = db.cursor()
    	select_if_in = "SELECT COUNT(*) FROM users where login = ?"
    	results = get_db().cursor().execute(
            select_if_in, (req['username'],)).fetchone()

    	# print('# Username: ', results['COUNT(*)'])
    	# Check if username count = 1 (Present) or 0 (Not Present)
    	if results['COUNT(*)'] == 0:
    		print('Username is not in DB')
    	else:
    		print('Username is present')
    	# username = 'nwchinn'
	    # response = requests.get("https://api.github.com/users/" + username)
	    # print("status code: ", response.status_code)
	    # user_data = response.json()
	    # print(user_data)
	    # print('Name: ', user_data['name'])
	    # print('login: ', user_data['login'])
	    # print('Followers: ', user_data['followers'])
	    # print('Following: ', user_data['following'])
	    # print('Public Repos: ', user_data['public_repos'])


    cur = db.cursor()
    cur = cur.execute('''SELECT * FROM users WHERE login= "nwchinn"''').fetchone()
    # context = cur.fetchall()
    print('type: ', type(cur))
    # context['login'] = user_data['login']
    context['login'] = 'nwchinn'
    return flask.render_template("index.html", **context)

# TO DO:
# @appname.app.route('/explore/')
# def show_explore():
#     """Desplay /explore/ route."""
#     db = insta485.model.get_db()
#     cur = db.cursor()
#     context = {}
#     print(context)
#     return flask.render_template("explore.html", **context)


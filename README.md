# reddit-saved-to-csv-and-pinboard

Exports saved posts and comments on Reddit to a csv file, and saves them as bookmarks on [Pinboard](https://pinboard.in/).

By default, this also saves the subreddit as a tag, and doesn't unsave posts/comments as it goes. Both behaviors can be deleted or uncommented as appropriate before running. Unsaving posts/comments is destructive but allows you to run the script multiple times and circumvent Reddit's API limits that restrict you to only downloading up to your most recent 1,000 saved items.

Forked from [AlkTheOrg/reddit-saved-to-csv](https://github.com/AlkTheOrg/reddit-saved-to-csv).

**Columns**: ID, Name, Subreddit, Type, URL, NoSFW
- ID: Starts from 1 and increments for each saved Post or Comment.
- Name: Title of the post.
- Subreddit: Display name of the subreddit.
- Type: Either #Comment or #Post.
- URL: Link of the comment or the post.
- NoSFW: True or False based on the post.

## How to Use
* Download or clone the code to your pc.
* Install [Python3](https://www.python.org/downloads/) and then install [praw](https://praw.readthedocs.io/en/latest/getting_started/installation.html).
* Go to https://www.reddit.com/prefs/apps and create a script.
  * Give any name and description.
  * Redirect uri: http://localhost:8080
  * Create
  * Text below "personal use script" is your client id. We'll need that and the secret.
* Open `reddit_saved_to_csv.py` file with any text editor.
* You'll see below lines at the top:
```python
client_id='' # Enter your client ID
client_secret='' # Enter your client secret
username='' # Enter reddit username
password='' # Enter reddit password
pinboard_token='' # Pinboard API key e.g. username:1341235
pinboard_tags='reddit_saved' # Tags used for Pinboard
```
* Enter the necessary information into the quotation marks.
* Save the .py file.
* Now you can run the script through command line/ VSCode/ Spyder etc.
* Wait until you get the "**COMPLETED!**" message.

# This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with HTML.
# This will be done by using python’s flask library.
# score_server - This function will serve the score. It will read the score from the scores file # and will return an HTML

from flask import Flask

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open("/Scores.txt", "r") as file:
            current_score = int(file.read())
            html_content = f"""
                            <html> 
                                <head> 
                                    <title>Scores Game</title> 
                                </head> 
                                <body> 
                                    <h1>The score is <div id="score">{current_score}</div></h1> 
                                </body> 
                            </html> """

    except FileNotFoundError:
        html_content = f"""
                        <html>
                            <head>
                                <title> Scores Game </title>
                            </head>
                            <body>
                            <body>
                                <h1><div id="score" style ="color:red">Error - File not found</div></h1>
                            </body>
                        </html>"""
    return html_content

# start the web server by running the score_server function
def start():
    app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    start()

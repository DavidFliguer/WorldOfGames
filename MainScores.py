from Score import get_current_score


def score_server():
    """
    Returns a string which is an HTML displaying the curent user score (Or error in case there was an issue)
    """
    base_html = """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            {}
        </body>
    </html>
    """
    score_line = ""
    try:
        cs = get_current_score()
        score_line = """<h1>The score is <div id="score">{}</div></h1>""".format(str(cs))
    except Exception as e:
        score_line = """<h1><div id="score" style="color:red">{}</div></h1>""".format(e)
    return base_html.format(score_line)

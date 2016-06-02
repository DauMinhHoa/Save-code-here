from flask import Flask, render_template

app = Flask(__name__)

class Movie:
    def __init__(self, title, img):
        self.title = title
        self.img = img
movie1 = Movie(' The girl next door',"https://upload.wikimedia.org/wikipedia/en/f/fc/Girl_Next_Door_movie.jpg")
movie2 = Movie(' panda',"http://eva-img.24hstatic.com/upload/2-2015/images/2015-05-11/1431312531-tac-hai-cua-mat-gau.jpg")
movie_list= [movie1,
             movie2,
             Movie('see summer',"https://theundercutmag.files.wordpress.com/2015/08/500-days-of-summer-500-days-of-summer-11124694-2559-1706.jpg")
             ]

@app.route('/')
def hello_world():
    return 'Hello Beep World!'
@app.route('/c4e')
def hello_c4e():
    return 'Hello Hoa!'

@app.route('/<name>')
def hello(name):
    return('Hello'+ ' ' +name)

@app.route('/movie')
def get_movie():
    return render_template('movie.html')

@app.route('/movie2')
def get_movie2():

    return render_template('movie_2.html',
                           title = 'Civil war',img='http://media.comicbook.com/2016/04/civil-war-cap-tony-179110.jpg')
@app.route('/movies')
def movies():
    return render_template("movies.html",movie_list=movie_list)
if __name__ == '__main__':
    app.run()

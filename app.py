from flask import Flask, render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


from core.views               import core 
from allapps.colorize.views   import colorize 
from allapps.enhance.views    import enhance 
from allapps.prediction.views import prediction 
from allapps.detection.views  import detection
from allapps.nlpapps.views    import nlpapps 


app.register_blueprint(core       , url_prefix="/core"       )
app.register_blueprint(colorize   , url_prefix="/colorize"   )
app.register_blueprint(enhance    , url_prefix="/enhance"    )
app.register_blueprint(prediction , url_prefix="/prediction" )
app.register_blueprint(detection  , url_prefix="/detection"  )
app.register_blueprint(nlpapps    , url_prefix="/nlpapps"    )


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()


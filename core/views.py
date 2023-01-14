
from flask import Blueprint, render_template

core = Blueprint('core',__name__, template_folder='templates')



@core.route('/services')
def services():
   return render_template('services.html')
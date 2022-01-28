from flask import Flask
from flask import request
from flask import jsonify

from peewee import *
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

db = PostgresqlDatabase('anime', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Country(BaseModel):
    show_name = CharField()
    capital = CharField(150)

db.connect()
db.drop_tables([Country])
db.create_tables([Country])

Country(show_name = 'Afghanistan', capital = 'Kabul').save()
Country(show_name = 'Albania', capital = 'Tirana').save()
Country(show_name = 'Algeria', capital = 'Algiers').save()
Country(show_name = 'Andorra', capital = 'Andorra la Vella').save()
Country(show_name = 'Angola', capital = 'Luanda').save()
Country(show_name = 'Antigua and Barbuda', capital = 'Saint John's').save()
Country(show_name = 'Argentina', capital = 'Buenos Aires').save()
Country(show_name = 'Armenia', capital = 'Yerevan').save()
Country(show_name = 'Australia', capital = 'Canberra').save()
Country(show_name = 'Austria', capital = 'Vienna').save()
Country(show_name = 'Azerbaijan', capital = 'Baku').save()
Country(show_name = 'Bahamas', capital = 'Nassau').save()
Country(show_name = 'Bahrain', capital = 'Manama').save()
Country(show_name = 'Bangladesh', capital = 'Dhaka').save()
Country(show_name = 'Barbados', capital = 'Bridgetown').save()
Country(show_name = 'Belarus', capital = 'Minsk').save()
Country(show_name = 'Belgium', capital = 'Brussels').save()
Country(show_name = 'Belize', capital = 'Belmopan').save()
Country(show_name = 'Benin', capital = 'Porto Novo').save()
Country(show_name = 'Bhutan', capital = 'Thimphu').save()
Country(show_name = 'Bolivia', capital = 'La Paz').save()
Country(show_name = 'Bosnia and Herzegovina', capital = 'Sarajevo').save()
Country(show_name = 'Botswana', capital = 'Gaborone').save()
Country(show_name = 'Brazil', capital = 'Brasilia').save()
Country(show_name = 'Brunei', capital = 'Bandar Seri Begawan').save()
Country(show_name = 'Bulgaria', capital = 'Sofia').save()
Country(show_name = 'Burkina Faso', capital = 'Ouagadougou').save()
Country(show_name = 'Burundi', capital = 'Gitega').save()
Country(show_name = 'Cambodia', capital = 'Phnom Penh').save()
Country(show_name = 'Cameroon', capital = 'Yaounde').save()


@app.route('/countries', methods=['GET'])
def countryy():
    country = []
    for capital in Country:
        country.append(model_to_dict(capital))
    return jsonify(country)

app.run(port=3000, debug=True)
from model.base import db
from model.base import app
from api.electric_fences_api import electric_fences_api
from api.electric_fences_services_api import electric_fences_services_api
from api.services_api import services_api
# app = Flask(__name__)

db.create_all()
db.session.commit()

app.register_blueprint(electric_fences_api)
app.register_blueprint(services_api)
app.register_blueprint(electric_fences_services_api)


if __name__ == '__main__':
    app.run(debug=True)

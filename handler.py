from mangum import Mangum
from api import create_app

handler = Mangum(app=create_app())

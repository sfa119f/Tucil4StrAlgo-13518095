from flask import Flask
from Config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)

from frontend import Main
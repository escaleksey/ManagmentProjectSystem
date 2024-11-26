import os

import sqlalchemy as sa
import sqlalchemy.orm as so
from run import app

app.config.from_object(os.environ['APP_SETTINGS'])


@app.shell_context_processor
def make_shell_context():
  return {'sa': sa, 'so': so}
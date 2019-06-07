import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

SECRET_KEY = '[O*z*),h{{3SOX9'

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'jdbc:postgresql://localhost:5432/flakdb'

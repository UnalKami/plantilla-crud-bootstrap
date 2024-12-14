from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load configuration from environment variables (avoid hardcoding credentials)
load_dotenv(dotenv_path='/.env')
SECRET_KEY = os.getenv("XXXX")
SECRET_HOST = os.getenv("XXXXX")
SECRET_MAIL = os.getenv("XXXXX")

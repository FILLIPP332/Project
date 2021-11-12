from flask import Flask, render_template
from webapp.weather import weather_by_city
from webapp.news import get_python_news
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hindex():
        tatle = "Новосто Python"
        weather = weather_by_city("Moscow,Russia")
        news_list = get_python_news()
        return render_template('index.html', page_tatle = tatle, weather=weather, news_list = news_list)
    return app

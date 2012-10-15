[Flask](http://flask.pocoo.org/) calls itself a micro-framework. That does *not* mean that it is not possible to build fully grown web applications. It means that it provides you with the most common and basic things you would expect from a web framework (e.g. URL routing and a bit more). For anything else it lets you choose the tools *you* want to use and goes out of your way. Nevertheless there are tons of extensions available.

## Example application

    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello World!"

    if __name__ == "__main__":
        app.run()
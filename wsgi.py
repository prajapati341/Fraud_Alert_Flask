from waitress import serve
import app1

if __name__ == "__main__":

    serve(app1.app, host='0.0.0.0', port=8080)
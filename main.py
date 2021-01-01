from application import init_app

app = init_app()

if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)
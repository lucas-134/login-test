from __init__ import create_app

app = create_app()

if __name__ == '__main__':
  # get rid of below in production
  app.run(host='0.0.0.0', debug=True)
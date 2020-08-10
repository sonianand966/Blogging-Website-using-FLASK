from flask_blog import app
#everything that is imported from flask_blog folder is imported from __init__.py


#if this python file is not called by any other module, and is run by python independently, then use debug mode
if(__name__ == '__main__'):
    app.run(debug=True)






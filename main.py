from flask import Flask, url_for, render_template, request, Response
from flask_static_compress import FlaskStaticCompress

mainApp = Flask(__name__)
mainApp.config['COMPRESSOR_DEBUG'] = mainApp.config.get('DEBUG')
mainApp.config['COMPRESSOR_STATIC_PREFIX'] = 'static'
mainApp.config['COMPRESSOR_OUTPUT_DIR'] = 'build'
mainApp.static_folder = 'static'
compress = FlaskStaticCompress(mainApp)

@mainApp.route("/", methods=['GET'])
def home():
    return render_template('/index.html', title="Site")

if __name__ == '__main__':
    mainApp.run()

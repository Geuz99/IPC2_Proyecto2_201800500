from flask import Flask, request, Response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origin": "*"}})

@app.route("/")
def index():
    return "PAGINA INICO"

@app.route('/datos', methods=['GET'])
def get_datos():
    save_file = open('chet.xml', 'r+')
    return Response(status=200,
                    response=save_file.read(),
                    content_type='application/xml')


@app.route('/datos', methods=['POST'])
def post_data():
    str_file = request.data.decode('utf-8')
    save_file = open('chet.xml', 'w+')
    save_file.write(str_file)
    save_file.close()
    return Response(status=204)

if __name__ == '__main__':
    app.run(debug=True)
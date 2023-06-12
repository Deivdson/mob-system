from app import app

@app.route("/")
def index():
    return "Hello world!"

@app.route('/lotes',methods=['GET'])
def getLotes():
    return 'Get all lotes!'

@app.route('/lote/create',methods=['POST'])
def createLotes():
    return 'Create new lote'

@app.route('/lote/update',methods=['UPDATE'])
def updateLotes():
    return 'Update lote'

@app.route('/lote/delete',methods=['DELETE'])
def deleteLotes():
    return 'Delete lote'
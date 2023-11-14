from flask import Flask, jsonify, request
app = Flask(__name__)
heart = [
    {
        "heart-id": "0",
        "date": "13/11/2023",
        "heart-rate": "100bpm"
        
    },
    {   
        "heart-id": "2",
        "date": "13/11/2023",
        "heart-rate": "200bpm"
    }
]

@app.route('/Q21', methods=['GET'])
def getheart():
    return jsonify(heart)

@app.route('/Q21', methods=['POST'])
def add_heart():
    new_heart = request.get_json()
    heart.append(new_heart)
    return{'heart-id':len(new_heart)},200

@app.route('/Q21/<int:index>', methods=['DELETE'])
def delete_heart(index):
    heart.pop(index)
    return 'Heart rate deleted', 200

if __name__=='__main__':
    app.run()
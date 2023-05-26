from flask import Flask

FAI=Flask(__name__)

@FAI.route('/wish')
def wish(name):
    return "Hello World"




@FAI.route('/good')
def good():
    return "Django And Flask"

if __name__=='__main__':
    FAI.run(debug=True)
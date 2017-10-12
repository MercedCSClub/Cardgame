

from flask import Flask,g,request
import json,uuid
app = Flask(__name__)
serverData={}
serverData["users"]=[]
serverData["games"]=[]
from random import randint

matches={"dog":{"cat":2.0,"dog":1.0,"person":3.0,"dogCatcher":0.3},"cat":{"cat":1.0,"dog":0.5,"person":0.3,"dogCatcher":0.0},
"person":{"cat":1.0,"dog":1.0,"person":1.0,"dogCatcher":0.3},"dogCatcher":{"cat":-0.3,"dog":3.0,"person":3.0,"dogCatcher":0}}
class card():
	def __init__(self,player,name,_class,power):
		self.id=uuid.uuid4()
		self.name=name
		self._class=_class
		self.power=power
		self.player=player
	def kill(self):
		self.dead=True
		self.player.removeCard(self.id)
	def attack(self,card):
		global matches
		#TODO:have defalut for nonexsistant cards
		card.power=card.power-(self.power*matches[self.name][card.name])
		if card.power<=0:
			card.kill()
		if self.power<=0:
			self.kill()
		
class user():
	def __init__(self,id):
		self.id=id
		self.cards=[]
		global matches
		self.newCards(matches,"match_p1")
	def newCards(self,matches_,matchPack):
		kk=[]
		newlist = list()
		for i in matches_.keys():
			newlist.append(i)
		i=0
		while(i<30):
			i+=1
			#self.cards
			#__init__(self,player,name,_class,power)
			u=card(self,newlist,matchPack,randint(3,40))
			self.cards.append(u)	
	def getUser(self,users,id):
		for user in users:
			if user.id==id:
				return user
	def getHand(self,size):
		return self.cards[len(self.cards)-size:len(self.cards)]
	def removeCard(self,cardID):
		i=0
		for card in self.cards:
			if(card.id==cardID):
				self.cards.pop(i)
				break
			i+=1
@app.route("/")
def hello():
	return "Welcome to Python Flask!"
 
@app.route('/signUpUser', methods=['POST','GET'])
def signUpUser():
	print(request.args["id"])
	global serverData
	serverData["users"].append(user(request.args['id']))
	#password = request.form['password']
	return json.dumps({'status':'OK'})
	
@app.route('/joingame', methods=['POST','GET'])
def joingame(): 
	global serverData
	serverid=0
	print(json.dumps({'status':'OK','serverid':serverid}))

	if(len(serverData["games"])==0):
		serverData["games"].append({"N.players":1,"players":[request.args['id']]})
		return json.dumps({'status':'OK','serverid':serverid})
	else:
		for server in serverData["games"]:	
			if server["N.players"]>int(request.args["min players"]) and server["N.players"]>int(request.args["max players"]):
				server["N.players"]+=1
				server["players"].append(request.args['id'])
				return json.dumps({'status':'OK','serverid':serverid})
			serverid+=1
		serverData["games"].append({"N.players":1,"players":[request.args['id']]})
		serverid+=1
		return json.dumps({'status':'OK','serverid':serverid})
	return json.dumps({'status':'OK','serverid':serverid})	
if __name__ == "__main__":
	app.run(host="0.0.0.0")
			

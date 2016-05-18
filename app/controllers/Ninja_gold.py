from system.core.controller import *
from time import strftime
import string, random

class Ninja_gold(Controller):
    def __init__(self, action):
        super(Ninja_gold, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        if not session.get('gold'):
            session['gold']=0
        if not session.get('activity'):
            session['activity']=[]
        return self.load_view('index.html', gold=session['gold'])

    def process(self):
        place = request.form['place']
        if place == 'farm':
            session['gold']+= random.randrange(10,21)
            session['activity'].append({'msg':"you went to the ninja farm - but why were you really there?", 'color':'green'})
        elif place == 'cave':
            session['gold']+= random.randrange(5,11)
            session['activity'].append({'msg':"you went to the ninja cave - why do you find more gold in a cave than a house?", 'color':'green'})
        elif place == 'house':
            session['gold']+= random.randrange(2,5)
            session['activity'].append({'msg':"you went to the ninja house - must be the house of poor people", 'color':'green'})
        elif place == 'casino':
            gold = random.randrange(0,2)
            if gold >= 1:
                session['gold']+=50
                session['activity'].append({'msg':"you went to the ninja casino and won 50 gold - HOW LONG WILL THAT LAST?!?!", 'color':'green'})
            else:
                session['gold']-=50
                session['activity'].append({'msg':"you went to the ninja casino - and YOU LOST 50 GOLD - TOTAL LOSER!", 'color':'red'})
            
        return self.load_view('index.html', gold=session['gold'], activity=session['activity'])
        # return self.load_view('test.html')

    def clear(self):
        session.clear()
        return redirect('/')
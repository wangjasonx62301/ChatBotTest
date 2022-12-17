from transitions.extensions import GraphMachine
from functools import partial


class Model:

    def Get_Todays_BBC_News(self, message):
        if message == "!news":
            return True

    def Add_News_To_Memory(self, message, index):
        if message == "!add" and 0 < index < 5:
            return True

    def Get_News_Memory(self, message):
        if message == "!review":
            return True

    def Delete_Memory(self, message):
        if message == "!del":
            return True
    
    def Delete_Memory_Index(self, index):
        if 0 < index < 5:
            return True

    def Go_Back(self):
        return True

model = Model()
machine = GraphMachine(model=model, states=['Line_bot', 'Get_Todays_BBC_News', 'Add_News_To_Memory', 'Get_News_Memory', 'Delete_Memory', 'Delete_Memory_Index'],
                       transitions=[
                           {'trigger': '!news', 'source': 'Line_bot', 'dest': 'Get_Todays_BBC_News', 'conditions': partial(model.Get_Todays_BBC_News, message = '!news')},
                           {'trigger': '!add x', 'source': 'Line_bot', 'dest': 'Add_News_To_Memory', 'conditions': partial(model.Add_News_To_Memory, message = "!add", index = [1, 2, 3, 4, 5])},
                           {'trigger': '!review', 'source': 'Line_bot', 'dest': 'Get_News_Memory', 'conditions': partial(model.Get_News_Memory, message = "!review")},
                           {'trigger': '!review', 'source': 'Line_bot', 'dest': 'Delete_Memory', 'conditions': partial(model.Delete_Memory, message = "!del")},
                           {'trigger': '!review', 'source': 'Delete_Memory', 'dest': 'Delete_Memory_Index', 'conditions': partial(model.Delete_Memory_Index, index = [1, 2, 3, 4, 5])},
                           {'trigger': '', 'source': 'Delete_Memory', 'dest': 'Line_bot', 'conditions': model.Go_Back},
                           {'trigger': '', 'source': 'Delete_Memory_Index', 'dest': 'Line_bot', 'conditions':  model.Go_Back},
                           {'trigger': '', 'source': 'Get_Todays_BBC_News', 'dest': 'Line_bot', 'conditions':  model.Go_Back},
                           {'trigger': '', 'source': 'Add_News_To_Memory', 'dest': 'Line_bot', 'conditions':  model.Go_Back},
                           {'trigger': '', 'source': 'Get_News_Memory', 'dest': 'Line_bot', 'conditions':  model.Go_Back},
                       ],
                       initial='Line_bot', show_conditions=True)

model.get_graph().draw('my_state_diagram.png', prog='dot')
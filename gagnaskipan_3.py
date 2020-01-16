class pizza():

    def __init__(self):
        self.__pizza_dict = dict()
        self.__unique_id = 0

    def add_pizza_toppings(self,list_of_toppings):
        #byrjar á state sem unserved og skilar unique ID
        self.__pizza_state = "unserved"

        self.__unique_id += 1

        self.__pizza_dict[self.__unique_id] = (self.__pizza_state,list_of_toppings)

        #Vantar ef það er meira en 3 toppings

        print(self.__pizza_dict)

        return "1345"

    def mark_as_served (self, pizza_id):
        #Fer í gegnum self.__pizza_dict og skiptir út unserved í served eða prentar error ef id er ekki til
        pass

    def __str__(self):
        return "MAMMA"

    def clear(self):
        #tæmir listann
        pass






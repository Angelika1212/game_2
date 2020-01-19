import sqlite3


class DATA_BASE():
    def __init__(self): 
        self.flag = True
        self.con = sqlite3.connect('для проекта.db')
        self.cur = self.con.cursor()        
        self.result = self.cur.execute('''SELECT * FROM Achievements''').fetchall()
        self.result = list(map(lambda x: list(x), self.result))      
        
    
    def add_to_date_base(self, inform, id_of_sentence):
        for i in range(len(self.result)):
            if inform in self.result[i]:
                self.flag = False
        if self.flag:
            self.cur.execute('''INSERT INTO Achievements(id, Name) VALUES(?, ?)''', 
                        (id_of_sentence, inform))
            self.con.commit()
            id_of_sentence += 1


def add_sentence(temperature, oxygen, speed_of_wind, water, magnetic_field, id_of_sentence):
    if temperature == 0:
        DATA_BASE().add_to_date_base('Ледниковый период', id_of_sentence)
    if temperature == 300:
        DATA_BASE().add_to_date_base('Огненная земля', id_of_sentence) 
    if (temperature == 300 or temperature == 0) and oxygen == 0:
        if speed_of_wind == 0 or speed_of_wind > 20 and water < 10:
            if magnetic_field == 'weak':
                DATA_BASE().add_to_date_base('Самые неблагоприятные условия', id_of_sentence)
    if 90 <= oxygen <= 100:
        DATA_BASE().add_to_date_base('Кислородная катастрофа', id_of_sentence)              

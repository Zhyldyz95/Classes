
class MacOS:
    def __init__(self, processor, memory,  video_card, hard_drive, motherboard, screen):
        self.processor = processor
        self.memory = memory
        self.video_card = video_card
        self.hard_drive = hard_drive
        self.motherboard = motherboard
        self.screen = screen
    def getinfo(self):
        print({
            'Процессор': self.processor,
            'Память': self.memory,
            'Тип видеокарты': self.video_card,
            'Жесткий диск': self.hard_drive,
            'Материнская плата': self.motherboard,
            'Экран': self.screen
        })

    def __str__(self):
        return 'Тут хранятся данные, запустите код'


MacBook_Air = MacOS('Apple M1', '8ГБ', 'встроенная', '256 ГБ', 'A2337', '13.3 дюймов, 2560x1600, широкоформатный' )
MacBook_Air.getinfo()




# Процессор Apple M1
# Память 8ГБ
# Тип видеокарты встроенная
#Жесткий диск 256 ГБ
#Материнская плата A2337
#Экран 13.3 дюймов, 2560x1600, широкоформатный

from mycroft import MycroftSkill, intent_file_handler


class Math(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('math.intent')
    def handle_math(self, message):
        self.speak_dialog('math')


def create_skill():
    return Math()


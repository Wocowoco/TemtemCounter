from pypresence import Presence

class DiscordPresence:
    def __init__(self):
        self.client_id = "651047461485281280" #TemtemCounter App ID
        self.RPC = Presence(client_id=self.client_id)
        self.RPC.connect()
    
    def update(self, _temToHunt, _encounters, _startTime):
        self.RPC.update(details="Hunting for a Luma " + _temToHunt.title(),
                        state="Encounters: " + str(_encounters),
                        large_image="temtem",
                        large_text="Temtem",
                        small_image="luma",
                        small_text="Luma",
                        start=_startTime)




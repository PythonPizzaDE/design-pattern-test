from dataclasses import dataclass

@dataclass
class EventHandler:
    listeners: dict

    def subscribe(self, event: str):
        if self.listeners.get(event):
            self.listeners['str']

handler = EventHandler({})

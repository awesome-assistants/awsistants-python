import pathlib
import json


# https://platform.openai.com/docs/api-reference/assistants/object
class Awsistant(dict):
    id: str
    emoji: str
    name: str
    instructions: str
    welcome_message: str
    parse_mode: str

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value


class Awsistants:
    def __init__(self):
        self.assistants = []
        self.assistants_file = (
            pathlib.Path(__file__).parent.resolve().joinpath("assistants.json")
        )

    def get_assistants(self) -> list[Awsistant]:
        if self.assistants:
            return self.assistants
        assistants = json.loads(
            self.assistants_file.read_text(), object_hook=lambda d: Awsistant(**d)
        )
        self.assistants = assistants
        return assistants

    def get_ids(self) -> list[str]:
        ids = []
        for x in self.get_assistants():
            ids.append(x.id)
        return ids

    def get_assistant(self, search_id) -> Awsistant:
        for x in self.get_assistants():
            if x.id == search_id:
                break
        else:
            x = None
        return x

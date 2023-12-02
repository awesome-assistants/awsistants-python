from .awsistants import Awsistants, Awsistant


def test_awsistants():
    aw = Awsistants()
    all_assistants = aw.get_assistants()
    assert isinstance(all_assistants, list)
    for x in all_assistants:
        assert isinstance(x, Awsistant)
        assert x.id
        assert x.emoji
        assert x.name
        assert x.welcome_message
        assert x.parse_mode in ["html", "markdown"]
        if x.id != "empty":
            assert x.instructions

    first = all_assistants[0]
    assistant = aw.get_assistant(first.id)
    assert isinstance(assistant, Awsistant)
    ids = aw.get_ids()
    assert isinstance(ids, list)
    for y in ids:
        assert isinstance(y, str)

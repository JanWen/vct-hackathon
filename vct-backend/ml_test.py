import ml
import uuid


def test_regions():
    """test that agent correctly retrn all regions"""
    response = ml.converse_agent(str(uuid.uuid1()), "tell me all the regions in the vct")
    assert all([x in response for x in ["BR", "NA", "LAN", "VN", "SEA", "INTL", "LAS", "LATAM", "EMEA", "JP", "KR"]])


def test_session_memory():
    session_id = str(uuid.uuid1())
    response1 = ml.converse_agent(session_id, "tell me some vct players?")
    print(response1)
    response2 = ml.converse_agent(session_id, "repeat my last quetion to me verbatum")
    assert "tell me some vct players" in response2    

# test_regions()
test_session_memory()

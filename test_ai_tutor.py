def test_basic_math():
    from ai_tutor import ask_tutor
    response = ask_tutor("What is 2 + 2?")
    assert "4" in response

def test_english_definition():
    from ai_tutor import ask_tutor
    response = ask_tutor("What is a noun?")
    assert "person" in response or "place" in response or "thing" in response

def test_addition_five_plus_five():
    from ai_tutor import ask_tutor
    response = ask_tutor("What is 5 + 5?")
    assert "10" in response

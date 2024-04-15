from main import make_upper_case

def test_upper_case():
    test_words = {
        "word": "WORD",
        "hola": "HOLA",
        "HELLO": "HELLO",
        "": ""
    }

    for input_, output_ in test_words.items():
        assert make_upper_case(input_) == output_
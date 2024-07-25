from mingk42_args_history.cli import hello_msg as msg

def test_hello():
    m=msg()
    assert m=="hello"

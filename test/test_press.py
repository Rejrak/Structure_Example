from pressButton.like_button import LikeState, press_many
import pytest
def test_empty_press():
    assert press_many(LikeState.empty, '') is LikeState.empty

def test_single_press():
    assert press_many(LikeState.empty, 'l') is LikeState.liked
    assert press_many(LikeState.empty, 'd') is LikeState.disliked

#Ho parametrizzato in modo tale che se uno dei test fallisce, gli altri test verranno comunque eseguiti
@pytest.mark.parametrize("test_input,expected",[
    ('ll',LikeState.empty),
    ('dd',LikeState.empty),
    ('ld',LikeState.disliked),
    ('dl',LikeState.liked),
    ('ldd',LikeState.empty),
    ('lldd', LikeState.empty),
    ('ddl',LikeState.liked)
])


def test_many_press(test_input,expected):
    assert press_many(LikeState.empty, test_input) is expected
    
@pytest.mark.skip(reason="regex not supported yet")
def test_regex_press():
    assert press_many(LikeState.empty, '[ld]*ddl') is LikeState.liked
    
#Da non usare in caso di eccezioni
@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1 
    
#Questo test fallira nel caso in cui l'eccezione non viene eseguita
def test_invalid_press():
    with pytest.raises(ValueError):
        press_many(LikeState.empty,'x')

#istanza di db_conn runnata come parametro di sessione nel file conftest.py
def test_db_press(db_conn):
    db_conn.read_press()
    assert ...
#capture_stdout configurato come parametro nel file conftest.py
def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"
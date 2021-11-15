from pressButton.like_button import LikeState, press_many

def test_press():
    assert press_many(LikeState.empty, '') is LikeState.empty
    assert press_many(LikeState.empty, 'l') is LikeState.liked
    assert press_many(LikeState.empty, 'd') is LikeState.disliked
    assert press_many(LikeState.empty, 'll') is LikeState.empty
    assert press_many(LikeState.empty, 'dd') is LikeState.empty
    assert press_many(LikeState.empty, 'ld') is LikeState.disliked
    assert press_many(LikeState.empty, 'dl') is LikeState.liked
    assert press_many(LikeState.empty, 'ldd') is LikeState.empty
    assert press_many(LikeState.empty, 'lldd') is LikeState.empty
    assert press_many(LikeState.empty, 'ddl') is LikeState.liked
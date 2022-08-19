import enum


class LikeState(enum.Enum):
    empty = enum.auto()
    liked = enum.auto()
    disliked = enum.auto()


press_like_transitions = {
        LikeState.empty: LikeState.liked,
        LikeState.liked: LikeState.empty,
        LikeState.disliked: LikeState.liked,
    }

press_dislike_transition = {
        LikeState.empty: LikeState.disliked,
        LikeState.liked: LikeState.disliked,
        LikeState.disliked: LikeState.empty,
    }


def press_like(s: LikeState) -> LikeState:
    return press_like_transitions[s]


def press_dislike(s: LikeState) -> LikeState:
    return press_dislike_transition[s]


def press_many(s: LikeState, press: str) -> LikeState:
    for c in press:
        c = c.lower()
        if c == "l":
            s = press_like(s)
        elif c == 'd':
            s = press_dislike(s)
        else:
            raise ValueError("invalid press")
    return s


def main():
    pass


if __name__ == '__main__':
    main()

import pynecone as pc


class State(pc.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


#str_increment = str("증가","utf-8") 한글 안되네....
str_increment = "increment"

def index():
    return pc.hstack(
        pc.button(
            "decrement",
            color_scheme="red",
            border_radius="2em",
            on_click=State.decrement,
        ),
        pc.heading(State.count, font_size="2em"),
        pc.button(
            str_increment,
            color_scheme="blue",
            border_radius="2em",
            on_click=State.increment,
        ),
    )


app = pc.App(state=State)
app.add_page(index)
app.compile()
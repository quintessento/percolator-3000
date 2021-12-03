from manim import *
import numpy as np


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

class GetHighlightedCellExample(Scene):
    def construct(self):
        # table = Table(
        #     [["First", "Second"],
        #     ["Third","Fourth"]],
        #     row_labels=[Text("R1"), Text("R2")],
        #     col_labels=[Text("C1"), Text("C2")])

        data = np.random.randint(3, size = (10, 10))
        res = data.astype(str)
        print(res.tolist())
        table = Table(res.tolist())

        self.add(table)

        cell = table.get_highlighted_cell((2, 2), color=None)
        table.add_to_back(cell)

        table = table.scale_to_fit_height(config.frame_height)
        scale_x = config.frame_width/table.width
        scale_y = config.frame_height/table.height
        scale = min([scale_x, scale_y])
        table = table.scale(scale)


        self.play(table.create())

        self.play(cell.animate.set_color(GREEN)) 
        self.wait()

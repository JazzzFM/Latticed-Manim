from manimlib.imports import *

def get_coords_from_csv(file_name):
    import csv
    coords = []
    with open(f'{file_name}.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            x,y = row
            coord = [float(x),float(y)]
            coords.append(coord)
    csvFile.close()
    return coords

class GraphFromData(GraphScene):
    # Covert the data coords to the graph points
    def get_points_from_coords(self,coords):
        return [self.coords_to_point(px,py)
            for px,py in coords
            ]

    # Return the dots of a set of points
    def get_dots_from_coords(self,coords,radius=0.1):
        points = self.get_points_from_coords(coords)
        dots = VGroup(*[
            Dot(radius=radius).move_to([px,py,pz])
            for px,py,pz in points
            ]
        )
        return dots

class CoordScreen(GraphFromData):
    def construct(self):
        screen_grid = ScreenGrid()
        self.add(screen_grid)
        coords = get_coords_from_csv("CUSTOM_GRAPHS_SCENE_VIDEO/data")
        pre_dots = dots = VGroup(*[
            Dot().move_to([px,py,0])
            for px,py in coords
            ]
        )
        pre_labels = VGroup(
            *[
                Text(f"({round(x)},{round(y)})",font="Times",stroke_width=0,color=GREEN)\
                .set_height(0.3).next_to([x,y,0],DOWN)
            for x,y in coords]
        )
        self.wait(8)
        self.play(FadeIn(pre_dots),FadeIn(pre_labels))
        self.wait(8)
        self.setup_axes(animate=True)
        self.wait(8)
        dots = self.get_dots_from_coords(coords)
        labels = pre_labels.copy()
        for label,coord in zip(labels,self.get_points_from_coords(coords)):
            label.next_to([coord[0],coord[1],0],DOWN)
        
        self.play(
            ReplacementTransform(pre_dots,dots),
            ReplacementTransform(pre_labels,labels),
            run_time=4
        )
        self.wait(8)


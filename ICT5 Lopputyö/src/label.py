class Label:
    def __init__(self, text, font, color, surface, position):
        self.text = text
        self.font = font
        self.color = color
        self.surface = surface
        self.position = position

    def update_label(self, text):
        self.text = text

    def render_label(self):
        self.surface.fill((0, 0, 0))
        rendered_text = self.font.render(self.text, True, self.color)
        self.surface.blit(rendered_text, (self.position[0], self.position[1]))

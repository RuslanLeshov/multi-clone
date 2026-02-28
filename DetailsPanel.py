from textual.widgets import  Label
from textual.containers import Container
from textual.content import ContentType


class DetailsPanel(Label):
  BORDER_TITLE = "Описание"
  
  def update_details(self, selected_row: str):
    self.update(f'Вы выбрали: {selected_row}')


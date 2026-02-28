from textual.widgets import  Label
from textual.containers import Container
from textual.content import ContentType
from Projects import data as projects_data, bundles as bundles_data


class DetailsPanel(Label):
  BORDER_TITLE = "Описание"
  
  def update_details(self, list_id: str, selected_row: str):
    if list_id == "select-items":
      text = projects_data[selected_row]["description"]
      self.update(text)
    elif list_id == "select-bundles":
      text = bundles_data[selected_row]["description"]
      self.update(text)


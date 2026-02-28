from textual.widgets import  Label

class SelectedListPanel(Label):
  BORDER_TITLE = "Выбрано"
  
  def update_details(self, selected_list: list[str]):
    text = "\n".join(selected_list)
    self.update(text)


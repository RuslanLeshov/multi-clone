from textual.app import App, ComposeResult
from textual.widgets import Static, Footer, Header, Label, TabbedContent
from textual.containers import Horizontal, Vertical, Container
from SelectionCatalog import SelectionCatalog
from SelectedListPanel import SelectedListPanel
from SearchBar import SearchBar
from DetailsPanel import DetailsPanel
from textual.widgets import SelectionList
from textual import on
from textual.events import Mount, Key
from textual.binding import Binding
from Projects import data as projects_data, bundles as bundles_data


class MultiCloneApp(App):

    BINDINGS = [
        Binding("q", "quit", "Выход"),
        Binding("tab", "switch_tab", "Сменить вкладку",
                show=True, priority=True),
        Binding("f", "focus_search", "Поиск", show=True),
        Binding("escape", "focus_list", "Список", show=True, priority=True),
    ]

    TITLE = "MultiClone"
    SUB_TITLE = "multiple git repositories cloner"
    CSS_PATH = "MultiClone.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield SelectionCatalog(id="selection-catalog")
            with Vertical():
                yield DetailsPanel()
                yield SelectedListPanel()

        yield Footer()

    @on(Mount)
    @on(SelectionList.SelectionHighlighted)
    @on(TabbedContent.TabActivated)
    def update_selection_details(self):
        active_tab = self.query_one(TabbedContent).active_pane
        selected_list = active_tab.query_one(SelectionList)

        if not selected_list:
            return

        selected_row = selected_list.highlighted_option.value

        self.query_one(DetailsPanel).update_details(
            selected_list.id, selected_row)

    @on(SelectionList.SelectedChanged)
    @on(TabbedContent.TabActivated)
    def update_selection_list_details(self):
        tabbed_content = self.query_one(TabbedContent)
        active_tab = tabbed_content.active_pane
        selected_list = active_tab.query_one(SelectionList)

        if not selected_list:
            return
        selected_ids = selected_list.selected

        selected_rows = None
        if tabbed_content.active == "projects":
            selected_rows = [projects_data[project_id]["name"]
                for project_id in selected_ids if project_id in projects_data]
        elif tabbed_content.active == "bundles":
            selected_rows = [bundles_data[bundle_id]["name"]
                for bundle_id in selected_ids if bundle_id in bundles_data]

        self.query_one(SelectedListPanel).update_details(selected_rows)

    def action_confirm_choice(self):
        active_tab = self.query_one(TabbedContent).active_pane
        selected_list = active_tab.query_one(SelectionList)

        if not selected_list:
            return

        selected_ids = selected_list.selected
        selected_rows = [
            option.prompt.plain for option in selected_list.options if option.value in selected_ids]

    def action_switch_tab(self):
        tabbed_content = self.query_one(TabbedContent)
        if tabbed_content.active == "projects":
            tabbed_content.active = "bundles"
        else:
            tabbed_content.active = "projects"
        tabbed_content.active_pane.query_one(SelectionList).focus()

    def action_focus_search(self):
        tabbed_content = self.query_one(TabbedContent)
        active_tab = tabbed_content.active_pane
        if tabbed_content.active == "projects":
            search_bar = active_tab.query_one(SearchBar)
            search_bar.focus()

    def action_focus_list(self):
        tabbed_content = self.query_one(TabbedContent)
        active_tab = tabbed_content.active_pane
        if tabbed_content.active == "projects":
            selection_list = active_tab.query_one(SelectionList)
            selection_list.focus()


    def check_action(
        self, action: str, parameters: tuple[object, ...]
    ) -> bool | None:  
        focused_id = self.focused.id if self.focused else None
        """Check if an action may run."""
        if action == "switch_tab" and focused_id not in ["select-items", "select-bundles"]:
            return False
        
        if action == "focus_search" and focused_id != "select-items":
            return False
        return True


if __name__ == "__main__":
    app = MultiCloneApp()
    app.run()

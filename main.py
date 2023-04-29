import flet as ft


class GreeterControl(ft.UserControl):
    def build(self):
        return ft.Text("Hello!")


class Counter(ft.UserControl):
    def build(self):

        self.counter = 0
        text = ft.Text(str(self.counter))

        async def add_click(e):
            self.counter += 1
            text.value = str(self.counter)
            await self.update_async()

        return ft.Row([GreeterControl(), text, ft.ElevatedButton("Add", on_click=add_click)])


async def main(page: ft.Page):
    await page.add_async(Counter())

ft.app(target=main, route_url_strategy="hash")

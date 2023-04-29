import flet as ft


class Main:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Routes Example"
        self.page.on_route_change = self.route_change
        self.page.on_view_pop = self.view_pop
        self.page.go(page.route)

    def route_change(self, route):
        self.page.views.clear()
        print(self.page.route)
        page_route = ft.TemplateRoute(self.page.route)
        print(page_route)
        if page_route.match("/"):
            self.page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Visit Store", on_click=lambda _: self.page.go("/store")),
                        ft.ElevatedButton("Visit Books", on_click=lambda _: self.page.go("/books/")),
                    ],
                )
            )
        elif page_route.match("/store"):
            self.page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: self.page.go("/")),
                    ],
                )
            )
        elif page_route.match("/books/:id"):
            self.page.views.append(
                ft.View(
                    "/books",
                    [
                        ft.AppBar(title=ft.Text("Books"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text(page_route.id),
                        ft.ElevatedButton("Go Home", on_click=lambda _: self.page.go("/")),
                    ],
                )
            )
        else:
            self.page.views.append(
                ft.View(
                    "/unknown",
                    [
                        ft.Text("Unknown route"),
                        ft.ElevatedButton("Go Home", on_click=lambda _: self.page.go("/")),
                    ],
                )
            )
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)


ft.app(target=Main, route_url_strategy="hash", web_renderer='')

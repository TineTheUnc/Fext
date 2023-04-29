import flet as ft
from typing import Dict, Callable
from .Rout import Rout


class App:
    def __init__(self, name: str):
        self.name: str = name
        self.__rout: Dict[str, Rout] = {}
        self.page = None

    def rout(self, path: str):

        def decorator(func: Callable):
            if path != "/":
                p = list(filter(lambda s: s and s != ' ', path.split("/")))
                if len(p) > 1:
                    raise "Rout error"
                p = ''.join(p)
                p = f'/{p}'
                if ' ' in p:
                    raise "Rout error"
                rout = Rout(path, 0, func)
                self.__rout.update({path: rout})
            else:
                rout = Rout(path, 0, func)
                self.__rout.update({path: rout})
            return rout

        return decorator

    async def route_change(self, route):
        path = self.page.route.split("/")
        path.pop(0)
        path = list(map(lambda p: f'/{p}', path))
        name = path[0]
        r = self.__rout.get(path[0], None)
        if r:
            c = await r.view(self.page, path)
        else:
            c = [
                    ft.Text("Unknown route"),
                ]
        self.page.views.append(
            ft.View(
                name,
                c,
            )
        )
        await self.page.update_async()

    async def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        await self.page.go_async(top_view.route)

    def run(self,
            name="",
            host=None,
            port=0,
            view = ft.FLET_APP,
            assets_dir=None,
            upload_dir=None,
            web_renderer="canvaskit",
            route_url_strategy="path",
            auth_token=None,
            ):
        async def main(page):
            self.page = page
            self.page.title = "Routes Example"
            self.page.on_route_change = self.route_change
            self.page.on_view_pop = self.view_pop
            await self.page.go_async(page.route)
        ft.app(main, name, host, port, view, assets_dir, upload_dir, web_renderer, route_url_strategy, auth_token)
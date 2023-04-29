import flet as ft
from typing import Callable, List


class Rout:
    def __init__(self, path: str, index: int, func: Callable):
        self.path: str = path
        self.index = index
        self.callable = func
        self.next_rout = {}

    def rout(self, path: str) -> Callable:

        def decorator(func: Callable) -> Rout:
            if path != "/":
                p = list(filter(lambda s: s and s != ' ', path.split("/")))
                if len(p) > 1:
                    raise "Rout error"
                p = ''.join(p)
                p = f'/{p}'
                if ' ' in p:
                    raise "Rout error"
                rout = Rout(path, self.index+1, func)
                self.next_rout.update({path: rout})
            else:
                rout = Rout(path, self.index+1, func)
                self.next_rout.update({path: rout})
            return rout

        return decorator

    async def view(self, page: ft.page, routs: List[str]):
        view = None
        routs.pop(0)
        if routs:
            print(self.next_rout)
            if self.next_rout:
                n_rout = self.next_rout.get(routs[0], None)
                if n_rout:
                    view = await n_rout.view(page, routs)
                else:
                    dy = list(filter(lambda k: ':' in k, self.next_rout.keys()))
                    view = await self.next_rout.get(dy[0], None).view(page, routs)
            else:
                view = ft.Text("Unknown route")
        if ':' in self.path:
            agr = page.route.split("/")[self.index+1]
            view = await self.callable(page, view, agr)
        else:
            view = await self.callable(page, view)
        return view

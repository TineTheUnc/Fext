from Fext import App
import flet as ft


app = App('test')


def g(page, path):
    async def go(_):
        await page.go_async(path)

    return go


@app.rout('/')
async def index(page, pack):
    return [
                ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Hello", on_click=g(page, "/hello")),
                ft.ElevatedButton("Book", on_click=g(page, "/book"))
            ]


@app.rout('/book')
async def book(page, pack):
    if pack:
        v = [
                ft.AppBar(title=ft.Text("Book"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("Book")
            ] + pack
    else:
        v = [
            ft.AppBar(title=ft.Text("Book"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text("Book"),
            ft.ElevatedButton("1", on_click=g(page, "/book/1"))
        ]
    return v


@book.rout('/:id')
async def index(page, pack, ids):
    return [
                ft.Text(str(ids)),
            ]


@app.rout('/hello')
async def hello(page, pack):
    if pack:
        v = [
                ft.AppBar(title=ft.Text("Hello"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("Hello")
            ] + pack
    else:
        v = [
            ft.AppBar(title=ft.Text("Hello"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text("Hello"),
            ft.ElevatedButton("Hello World", on_click=g(page, "/hello/world"))
        ]
    return v


@hello.rout('/world')
async def world(page, pack):
    if pack:
        v = [
                ft.AppBar(title=ft.Text("Hello"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text("world")
            ] + pack
    else:
        v = [
            ft.AppBar(title=ft.Text("Hello"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text("world"),
            ft.ElevatedButton("Hello World Test", on_click=g(page, "/hello/world/test"))
        ]
    return v


@world.rout('/:id')
async def ids(page, pack, ids):
    if pack:
        v = [
                ft.AppBar(title=ft.Text("Hello"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.Text(str(ids))
            ] + pack
    else:
        v = [
            ft.AppBar(title=ft.Text("Hello"), bgcolor=ft.colors.SURFACE_VARIANT),
            ft.Text(str(ids)),
            ft.ElevatedButton("Hello World Test gg", on_click=g(page, "/hello/world/test/gg"))
        ]
    return v


@ids.rout('/:gg')
async def gg(page, pack,gg):
    return [
                ft.Text(str(gg)),
            ]


app.run(route_url_strategy="hash")

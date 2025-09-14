import flets as ft
import time


def main(page: ft.Page):
    page.title = "¿Me perdonas?"
    page.bgcolor=ft.Colors.RED_ACCENT_100
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical:alignment = ft.MainAxisAlignment.CENTER
    
    
    
    label=ft.Text(
        "Me perdonas?"
        style=ft.TextStyle(size=40, weight="bold")

    )
    
    image = ft.Image(src="triste.png", widht=200, height=200)
    
    button_yes=ft.ElevatedButton(text="si",color=ft.Colors.GREEN,widht=100,height=50)
    button_no=ft.ElevatedButton(text="No",color=ft.Colors.RED,width=100,height=50)
    button_maybe=ft.ElevatedButton(text="Quizas,color=ft.Colors.YELLOW,width=100,height=50")
    
    
    def no_click(e):
        button_yes.width+20
        button_yes.height=+=10
        page.update()
        
        
        def yes_click(e):
            image.src = "feliz.png"
            image.update()
            
        def maybe_click(e):
            image.src="Quiza.png"
            image.update()
            
            time.sleep(2)
            resset_app()
            
        def resset_app():
            image.src = "triste.png"
            button_yes.widht=100
            button_yes.height=50
            page.update()
            
            
        button_no.on_click = no_click
        button_yes.on_click =yes_click
        button_maybe.on_click = maybe_click
        
        page.add(
            ft.Column(
                [
                    label,
                    image,
                    ft.Row([
                        button_yes,
                        button_no,
                        button_maybe
                    ],
                           alignment=ft.MainAxisAlignment.CENTER,
                    ,
                ],
                alignment= MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            )      
        )
            
            
 ft.app(main)
    
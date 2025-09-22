import flet as ft

def main(page: ft.Page):
    page.title = "♻️ Reto: Decisiones Interactivas"
    page.window_width = 420
    page.window_height = 720

    estado = {"actual": "inicio"}  # estado inicial

    titulo = ft.Text("♻️ Decisiones Interactivas", size=22, weight="bold")
    texto = ft.Text("", size=18)
    imagen = ft.Image(src="", width=280, height=180, fit=ft.ImageFit.CONTAIN, visible=False)

    # Botones
    btn_si = ft.ElevatedButton("Sí")
    btn_no = ft.ElevatedButton("No")
    btn_reset = ft.TextButton("Reiniciar", icon=ft.Icons.REFRESH)
    botones = ft.Row([btn_si, btn_no], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    # --- PANTALLAS ---
    def mostrar_inicio():
        estado["actual"] = "inicio"
        page.bgcolor = None
        texto.value = "🤖 ¿Ayudas al robot a reciclar hoy?"
        imagen.src = "robot.png"
        imagen.visible = True
        btn_si.visible = True
        btn_no.visible = True
        page.update()

    def a_pregunta2_si():
        estado["actual"] = "p2_si"
        texto.value = "📄 Tienes papel y plástico. ¿Empiezas separando el papel?"
        imagen.src = "papel.png"
        page.update()

    def a_pregunta3_si():
        estado["actual"] = "p3_si"
        texto.value = "🍼 Ahora encuentras vidrio. ¿Lo colocas en el contenedor verde?"
        imagen.src = "aldea.png"
        page.update()

    def a_pregunta4_si():
        estado["actual"] = "p4_si"
        texto.value = "🔋 ¡Bien! Encuentras pilas usadas. ¿Las guardas en una bolsa especial?"
        imagen.src = "pila.png"
        page.update()

    def a_pregunta5_si():
        estado["actual"] = "p5_si"
        texto.value = "🍎 Te dan restos de comida. ¿Los pones en composta?"
        imagen.src = "composta.png"
        page.update()

    def final_bueno():
        estado["actual"] = "final_bueno""
        texto.value = "🎉 ¡Excelente! Has reciclado todo correctamente."
        page.bgcolor = ft.Colors.GREEN_200
        imagen.src = "tesoro.png"
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    def final_medio():
        estado["actual"] = "final_medio"
        texto.value = "😅 Casi... Te faltó separar algunos residuos."
        page.bgcolor = ft.Colors.AMBER_200
        imagen.src = "descanso.png"
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    def final_malo():
        estado["actual"] = "final_malo"
        texto.value = "💀 No participaste. El robot se quedó solo..."
        page.bgcolor = ft.Colors.RED_200
        imagen.src = "mounstruo.png"
        btn_si.visible = False
        btn_no.visible = False
        page.update()

    # --- LÓGICA DE BOTONES ---
    def on_si(e):
        if estado["actual"] == "inicio":
            a_pregunta2_si()
        elif estado["actual"] == "p2_si":
            a_pregunta3_si()
        elif estado["actual"] == "p3_si":
            a_pregunta4_si()
        elif estado["actual"] == "p4_si":
            a_pregunta5_si()
        elif estado["actual"] == "p5_si":
            final_bueno()

    def on_no(e):
        if estado["actual"] == "inicio":
            final_malo()
        elif estado["actual"] == "p2_si":
            final_medio()
        elif estado["actual"] == "p3_si":
            final_medio()
        elif estado["actual"] == "p4_si":
            final_malo()
        elif estado["actual"] == "p5_si":
            final_medio()

    def on_reset(e):
        mostrar_inicio()

    # Eventos
    btn_si.on_click = on_si
    btn_no.on_click = on_no
    btn_reset.on_click = on_reset

    # Layout
    page.add(
        ft.Column(
            [titulo, texto, imagen, botones, btn_reset],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=16,
            expand=True
        )
    )

    mostrar_inicio()

ft.app(target=main)
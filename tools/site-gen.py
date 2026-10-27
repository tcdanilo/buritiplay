"""Gera o site do estúdio Buriti Play (GitHub Pages): início, suporte, política de privacidade e exclusão de conta em 3 idiomas."""
import html, sys, os

OUT = sys.argv[1]
EMAIL = "danilotiago3@hotmail.com"

CSS = """
:root{--ink:#2B2F3A;--muted:#5d6472;--green:#1f7a45;--orange:#e8771a;--bg:#fffaf1;--card:#ffffff;--line:#eadfc9}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
header{background:#fff;border-bottom:1px solid var(--line)}
.bar{max-width:760px;margin:0 auto;padding:12px 16px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.bar a.home img{height:56px;display:block}
nav a{color:var(--green);text-decoration:none;font-weight:600;margin-left:14px}
nav a:hover{text-decoration:underline}
main{max-width:760px;margin:0 auto;padding:24px 16px 48px}
h1{font-size:30px;line-height:1.2;margin:8px 0 4px}
h2{font-size:21px;margin:28px 0 6px}
p,li{color:var(--ink)}
.muted{color:var(--muted);font-size:15px}
a{color:var(--green)}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px;display:flex;gap:18px;align-items:center;margin:20px 0}
.card img{width:96px;height:96px;border-radius:22px;flex:none}
.card h2{margin:0 0 4px}
.langs a{display:inline-block;margin:4px 10px 4px 0}
.hero{text-align:center;padding:24px 0 8px}
.hero img{width:220px;max-width:70%}
@media(max-width:560px){.card{flex-direction:column;text-align:center}}
footer{max-width:760px;margin:0 auto;padding:0 16px 32px;color:var(--muted);font-size:14px}
"""

def page(name, title, lang, body, nav):
    links = " ".join(f'<a href="{h}">{html.escape(t)}</a>' for h, t in nav)
    doc = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="icon" href="sniff-and-sort.png">
<style>{CSS}</style>
</head>
<body>
<header><div class="bar"><a class="home" href="index.html"><img src="logo.png" alt="Buriti Play"></a><nav>{links}</nav></div></header>
<main>
{body}
</main>
<footer>© 2026 Buriti Play · <a href="mailto:{EMAIL}">{EMAIL}</a></footer>
</body>
</html>
"""
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(doc)

def md(text):
    """Parágrafos e listas simples: linha começando com '- ' vira item; '## ' vira título."""
    out, items = [], []
    def flush():
        if items:
            out.append("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>")
            items.clear()
    for block in text.strip().split("\n"):
        line = block.strip()
        if not line:
            flush(); continue
        line = html.escape(line).replace("[EMAIL]", f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
        # **negrito**
        while "**" in line:
            line = line.replace("**", "<strong>", 1).replace("**", "</strong>", 1)
        if line.startswith("- "):
            items.append(line[2:])
        elif line.startswith("## "):
            flush(); out.append(f"<h2>{line[3:]}</h2>")
        else:
            flush(); out.append(f"<p>{line}</p>")
    flush()
    return "\n".join(out)

PRIVACY = {
"en": ("privacy.html", "Privacy Policy", "Last updated: October 27, 2026", """
Sniff & Sort is a game by Buriti Play, the studio of Danilo Costa Tiago ("we"). This policy explains what data the game uses, why, and how you can delete it.

## 1. Data we collect
- **Game account:** when you open the game for the first time, we create an anonymous account, without asking for an email, name or password. If you use Game Center, we store your Game Center identifier so you can recover your progress.
- **Progress and profile:** levels played, results, stars, coins, decorated cities, settings, the nickname and avatar you choose, your in-game friends and your weekly tournament points.
- **Purchases:** which items you bought in the game. Payment is handled by Apple or Google Play; we never receive your card details.
- **Game usage:** events such as starting and finishing a level, so we can see where the game is too hard and improve it.
- **Device:** the code used to send notifications (if you allow them), the time zone, the language and the game version.
- **Ads:** the game shows ads from Google AdMob. Google collects the device's advertising identifier (on iPhone, only if you allow tracking), the IP address (which gives an approximate location), which ads you saw and tapped, and diagnostic data about the ads.
We do not collect your precise location, contacts, photos, real name, email or phone number.

## 2. How we use it
To make the game work (saving and recovering progress, rankings, friends, the tournament and purchases), to send the notifications you allowed, to prevent cheating in the rankings and to improve the game. Google uses the ad data above to show ads, measure them and prevent fraud. If you allow tracking, the ads can be based on your interests; if not, you still see ads, just not personalized ones. We do not sell your data.

## 3. What other players see
Your nickname, avatar, level reached, stars and points appear in the rankings and to your in-game friends.

## 4. Companies that help us
The data is stored with services we hire, which process it only to provide their service to us: Supabase (server and database), Google Firebase (usage analytics and notifications), RevenueCat (purchase records), Google AdMob (ads) Apple (Game Center and App Store) and Google (Google Play). Google's policy for ads is at policies.google.com/technologies/partner-sites. These servers may be located outside your country.

## 5. How long we keep it
For as long as your account exists. When you delete your account, we delete your profile, progress, results, friends and the devices linked to it.

## 6. Your rights
You can delete your account and your data at any time inside the game, in Profile › Delete account (step by step at tcdanilo.github.io/buritiplay/delete-account.html). To ask for a copy of your data, correct it or ask any question, write to [EMAIL]. You can also turn off notifications in your phone's settings. To stop ad tracking: on iPhone, Settings › Privacy & Security › Tracking; on Android, Settings › Privacy › Ads › Delete advertising ID. These rights follow the LGPD (Brazil) and the GDPR (European Union).

## 7. Children
The game is not directed at children under 13 and does not knowingly collect data from children. If you believe a child has sent us data, write to [EMAIL] and we will delete it.

## 8. Changes
If this policy changes, we will update this page and the date at the top.

**Contact:** Buriti Play, Danilo Costa Tiago, [EMAIL].
"""),
"pt": ("privacidade.html", "Política de Privacidade", "Última atualização: 27 de outubro de 2026", """
O Sniff & Sort é um jogo da Buriti Play, estúdio de Danilo Costa Tiago ("nós"). Esta política explica quais dados o jogo usa, para quê e como você pode apagá-los.

## 1. Dados que coletamos
- **Conta do jogo:** ao abrir o jogo pela primeira vez, criamos uma conta anônima, sem pedir e-mail, nome ou senha. Se você usa o Game Center, guardamos o seu identificador do Game Center para recuperar o seu progresso.
- **Progresso e perfil:** fases jogadas, resultados, estrelas, moedas, cidades decoradas, configurações, o apelido e o avatar que você escolher, seus amigos no jogo e seus pontos no torneio semanal.
- **Compras:** quais itens você comprou dentro do jogo. O pagamento é feito pela Apple ou pelo Google Play; nós não recebemos dados do seu cartão.
- **Uso do jogo:** eventos como início e fim de fase, para entender onde o jogo está difícil demais e melhorá-lo.
- **Aparelho:** o código para enviar notificações (se você permitir), o fuso horário, o idioma e a versão do jogo.
- **Anúncios:** o jogo mostra anúncios do Google AdMob. O Google coleta o identificador de publicidade do aparelho (no iPhone, só se você permitir o rastreamento), o endereço IP (que dá uma localização aproximada), quais anúncios você viu e tocou, e dados de diagnóstico dos anúncios.
Não coletamos sua localização exata, contatos, fotos, nome real, e-mail ou telefone.

## 2. Para que usamos
Para o jogo funcionar (salvar e recuperar o progresso, rankings, amigos, torneio e compras), para mandar os avisos que você permitiu, para evitar trapaças nos rankings e para melhorar o jogo. O Google usa os dados de anúncios acima para mostrar anúncios, medi-los e evitar fraudes. Se você permitir o rastreamento, os anúncios podem seguir os seus interesses; se não permitir, você continua vendo anúncios, só que não personalizados. Não vendemos seus dados.

## 3. O que os outros jogadores veem
Seu apelido, avatar, fase alcançada, estrelas e pontos aparecem nos rankings e para os seus amigos no jogo.

## 4. Empresas que nos ajudam
Os dados ficam guardados com serviços contratados por nós, que os tratam só para nos prestar o serviço: Supabase (servidor e banco de dados), Google Firebase (análise de uso e envio de notificações), RevenueCat (registro das compras), Google AdMob (anúncios) Apple (Game Center e App Store) e Google (Google Play). A política do Google para anúncios está em policies.google.com/technologies/partner-sites. Esses servidores podem ficar fora do Brasil.

## 5. Por quanto tempo guardamos
Enquanto a sua conta existir. Quando você apaga a conta, apagamos o seu perfil, progresso, resultados, amigos e aparelhos ligados a ela.

## 6. Seus direitos
Você pode apagar a sua conta e os seus dados a qualquer momento dentro do jogo, em Perfil › Apagar conta (passo a passo em tcdanilo.github.io/buritiplay/delete-account.html). Para pedir uma cópia dos seus dados, corrigi-los ou tirar dúvidas, escreva para [EMAIL]. Você também pode desligar as notificações nos ajustes do celular. Para parar o rastreamento de anúncios: no iPhone, Ajustes › Privacidade e Segurança › Rastreamento; no Android, Configurações › Privacidade › Anúncios › Excluir ID de publicidade. Esses direitos seguem a LGPD (Brasil) e o GDPR (União Europeia).

## 7. Crianças
O jogo não é voltado para crianças menores de 13 anos e não coleta, de propósito, dados de crianças. Se você acha que uma criança nos mandou dados, escreva para [EMAIL] e apagamos.

## 8. Mudanças
Se esta política mudar, atualizamos esta página e a data no topo.

**Contato:** Buriti Play, Danilo Costa Tiago, [EMAIL].
"""),
"es": ("privacidad.html", "Política de Privacidad", "Última actualización: 27 de octubre de 2026", """
Sniff & Sort es un juego de Buriti Play, el estudio de Danilo Costa Tiago ("nosotros"). Esta política explica qué datos usa el juego, para qué y cómo puedes eliminarlos.

## 1. Datos que recopilamos
- **Cuenta del juego:** al abrir el juego por primera vez, creamos una cuenta anónima, sin pedir correo electrónico, nombre ni contraseña. Si usas Game Center, guardamos tu identificador de Game Center para recuperar tu progreso.
- **Progreso y perfil:** niveles jugados, resultados, estrellas, monedas, ciudades decoradas, ajustes, el apodo y el avatar que elijas, tus amigos en el juego y tus puntos en el torneo semanal.
- **Compras:** qué artículos compraste en el juego. El pago lo gestiona Apple o Google Play; nunca recibimos los datos de tu tarjeta.
- **Uso del juego:** eventos como empezar y terminar un nivel, para ver dónde el juego es demasiado difícil y mejorarlo.
- **Dispositivo:** el código para enviar notificaciones (si lo permites), la zona horaria, el idioma y la versión del juego.
- **Anuncios:** el juego muestra anuncios de Google AdMob. Google recopila el identificador de publicidad del dispositivo (en iPhone, solo si permites el rastreo), la dirección IP (que da una ubicación aproximada), qué anuncios viste y tocaste, y datos de diagnóstico de los anuncios.
No recopilamos tu ubicación exacta, contactos, fotos, nombre real, correo electrónico ni teléfono.

## 2. Para qué los usamos
Para que el juego funcione (guardar y recuperar el progreso, rankings, amigos, torneo y compras), para enviar los avisos que permitiste, para evitar trampas en los rankings y para mejorar el juego. Google usa los datos de anuncios anteriores para mostrar anuncios, medirlos y evitar fraudes. Si permites el rastreo, los anuncios pueden basarse en tus intereses; si no, sigues viendo anuncios, solo que no personalizados. No vendemos tus datos.

## 3. Qué ven los demás jugadores
Tu apodo, avatar, nivel alcanzado, estrellas y puntos aparecen en los rankings y para tus amigos en el juego.

## 4. Empresas que nos ayudan
Los datos se guardan en servicios que contratamos, que los tratan solo para prestarnos su servicio: Supabase (servidor y base de datos), Google Firebase (análisis de uso y envío de notificaciones), RevenueCat (registro de compras), Google AdMob (anuncios) Apple (Game Center y App Store) y Google (Google Play). La política de Google para anuncios está en policies.google.com/technologies/partner-sites. Estos servidores pueden estar fuera de tu país.

## 5. Cuánto tiempo los guardamos
Mientras exista tu cuenta. Cuando eliminas tu cuenta, eliminamos tu perfil, progreso, resultados, amigos y los dispositivos vinculados a ella.

## 6. Tus derechos
Puedes eliminar tu cuenta y tus datos en cualquier momento dentro del juego, en Perfil › Eliminar cuenta (paso a paso en tcdanilo.github.io/buritiplay/delete-account.html). Para pedir una copia de tus datos, corregirlos o hacer cualquier pregunta, escribe a [EMAIL]. También puedes desactivar las notificaciones en los ajustes del teléfono. Para detener el rastreo de anuncios: en iPhone, Ajustes › Privacidad y seguridad › Rastreo; en Android, Ajustes › Privacidad › Anuncios › Borrar ID de publicidad. Estos derechos siguen la LGPD (Brasil) y el RGPD (Unión Europea).

## 7. Niños
El juego no está dirigido a menores de 13 años y no recopila, a sabiendas, datos de niños. Si crees que un niño nos envió datos, escribe a [EMAIL] y los eliminaremos.

## 8. Cambios
Si esta política cambia, actualizaremos esta página y la fecha de arriba.

**Contacto:** Buriti Play, Danilo Costa Tiago, [EMAIL].
"""),
}

SUPPORT = {
"en": ("Support", """
Need help with Sniff & Sort? Write to [EMAIL] and tell us your device model and, if you can, your friend code (Profile screen). We answer in English, Portuguese and Spanish.

## Common questions
- **I changed iPhones. How do I keep my progress?** Sign in to Game Center on both phones before opening the game; your progress is saved on our server and comes back.
- **A purchase didn't arrive.** Close and reopen the game. If it still doesn't show, write to us. Refunds are handled by Apple at reportaproblem.apple.com, or by Google Play at play.google.com (Order history).
- **How do I delete my account?** In the game, go to Profile › Delete account. This deletes your progress and data from our server. More details on the Delete account page.
"""),
"pt": ("Suporte", """
Precisa de ajuda com o Sniff & Sort? Escreva para [EMAIL] e diga o modelo do seu aparelho e, se puder, o seu código de amigo (tela de Perfil). Respondemos em português, inglês e espanhol.

## Dúvidas comuns
- **Troquei de iPhone. Como mantenho o progresso?** Entre no Game Center nos dois aparelhos antes de abrir o jogo; seu progresso fica salvo no nosso servidor e volta.
- **Uma compra não chegou.** Feche e abra o jogo de novo. Se ainda não aparecer, escreva para nós. Reembolsos são feitos pela Apple em reportaproblem.apple.com ou pelo Google Play em play.google.com (Histórico de pedidos).
- **Como apago a minha conta?** No jogo, vá em Perfil › Apagar conta. Isso apaga o seu progresso e os seus dados do nosso servidor. Mais detalhes na página Apagar conta.
"""),
"es": ("Soporte", """
¿Necesitas ayuda con Sniff & Sort? Escribe a [EMAIL] y dinos el modelo de tu dispositivo y, si puedes, tu código de amigo (pantalla de Perfil). Respondemos en español, inglés y portugués.

## Preguntas frecuentes
- **Cambié de iPhone. ¿Cómo conservo mi progreso?** Inicia sesión en Game Center en los dos teléfonos antes de abrir el juego; tu progreso se guarda en nuestro servidor y vuelve.
- **Una compra no llegó.** Cierra y vuelve a abrir el juego. Si sigue sin aparecer, escríbenos. Los reembolsos los gestiona Apple en reportaproblem.apple.com o Google Play en play.google.com (Historial de pedidos).
- **¿Cómo elimino mi cuenta?** En el juego, ve a Perfil › Eliminar cuenta. Esto elimina tu progreso y tus datos de nuestro servidor. Más detalles en la página Eliminar cuenta.
"""),
}

DELETE = {
"en": ("Delete your Sniff & Sort account", """
Sniff & Sort is a game by Buriti Play (Danilo Costa Tiago). The game creates an anonymous account the first time you open it. You can delete this account and its data at any time.

## Delete it in the game
- Open Sniff & Sort.
- On the bar at the bottom of the screen, tap **Crew** to open your **Profile**.
- Tap **Delete account**, then **Delete forever**.
The deletion is immediate and cannot be undone.

## What is deleted
Your profile (nickname and friend code), progress, stars, coins, decorated cities, level results, tournament points, friends list and the devices linked to the account (including the notification code).

## What is kept
- Records of purchases kept by Apple, Google Play and RevenueCat, which the stores need for refunds and taxes. They are not linked to your name.
- Game usage statistics in Google Firebase, which are not linked to your name and are deleted automatically by Google.

## No longer have the game?
Write to [EMAIL] with the subject "Delete account" and your friend code (Profile screen), if you have it. We delete the account within 30 days and reply to confirm.
"""),
"pt": ("Apagar a sua conta do Sniff & Sort", """
O Sniff & Sort é um jogo da Buriti Play (Danilo Costa Tiago). O jogo cria uma conta anônima na primeira vez que você o abre. Você pode apagar essa conta e os dados dela quando quiser.

## Apagar pelo jogo
- Abra o Sniff & Sort.
- Na barra de baixo da tela, toque em **Equipe** para abrir o seu **Perfil**.
- Toque em **Apagar conta** e depois em **Apagar para sempre**.
A exclusão é imediata e não pode ser desfeita.

## O que é apagado
O seu perfil (apelido e código de amigo), progresso, estrelas, moedas, cidades decoradas, resultados das fases, pontos do torneio, lista de amigos e os aparelhos ligados à conta (inclusive o código das notificações).

## O que fica guardado
- O registro das compras guardado pela Apple, pelo Google Play e pelo RevenueCat, que as lojas precisam para reembolsos e impostos. Ele não tem o seu nome.
- As estatísticas de uso do jogo no Google Firebase, que não têm o seu nome e são apagadas sozinhas pelo Google.

## Não tem mais o jogo?
Escreva para [EMAIL] com o assunto "Apagar conta" e o seu código de amigo (tela de Perfil), se tiver. Apagamos a conta em até 30 dias e respondemos confirmando.
"""),
"es": ("Eliminar tu cuenta de Sniff & Sort", """
Sniff & Sort es un juego de Buriti Play (Danilo Costa Tiago). El juego crea una cuenta anónima la primera vez que lo abres. Puedes eliminar esta cuenta y sus datos en cualquier momento.

## Eliminarla en el juego
- Abre Sniff & Sort.
- En la barra de abajo de la pantalla, toca **Equipo** para abrir tu **Perfil**.
- Toca **Eliminar cuenta** y luego **Eliminar para siempre**.
La eliminación es inmediata y no se puede deshacer.

## Qué se elimina
Tu perfil (apodo y código de amigo), progreso, estrellas, monedas, ciudades decoradas, resultados de los niveles, puntos del torneo, lista de amigos y los dispositivos vinculados a la cuenta (incluido el código de notificaciones).

## Qué se conserva
- El registro de compras que guardan Apple, Google Play y RevenueCat, que las tiendas necesitan para reembolsos e impuestos. No está vinculado a tu nombre.
- Las estadísticas de uso del juego en Google Firebase, que no están vinculadas a tu nombre y Google elimina automáticamente.

## ¿Ya no tienes el juego?
Escribe a [EMAIL] con el asunto "Eliminar cuenta" y tu código de amigo (pantalla de Perfil), si lo tienes. Eliminamos la cuenta en un plazo de 30 días y respondemos para confirmarlo.
"""),
}

LANG_NAME = {"en": "English", "pt": "Português", "es": "Español"}
NAV = [("support.html", "Support"), ("privacy.html", "Privacy")]

for code, (name, title, updated, text) in PRIVACY.items():
    others = " · ".join(f'<a href="{PRIVACY[c][0]}">{LANG_NAME[c]}</a>' for c in PRIVACY if c != code)
    body = f'<h1>{html.escape(title)}</h1>\n<p class="muted">Sniff & Sort · {html.escape(updated)} · {others}</p>\n' + md(text)
    page(name, f"{title} · Sniff & Sort", {"pt": "pt-BR"}.get(code, code), body, NAV)

parts = []
for code, (title, text) in SUPPORT.items():
    parts.append(f'<section id="{code}" lang="{code}"><h1>{html.escape(title)}</h1>\n{md(text)}</section>')
jump = " · ".join(f'<a href="#{c}">{LANG_NAME[c]}</a>' for c in SUPPORT)
page("support.html", "Support · Sniff & Sort", "en", f'<p class="muted">{jump}</p>\n' + "\n".join(parts), NAV)

parts = []
for code, (title, text) in DELETE.items():
    parts.append(f'<section id="{code}" lang="{code}"><h1>{html.escape(title)}</h1>\n{md(text)}</section>')
jump = " · ".join(f'<a href="#{c}">{LANG_NAME[c]}</a>' for c in DELETE)
page("delete-account.html", "Delete account · Sniff & Sort", "en", f'<p class="muted">{jump}</p>\n' + "\n".join(parts), NAV)

index = f"""<div class="hero"><img src="logo.png" alt="Buriti Play"></div>
<p>Buriti Play is a small game studio from Buritis, Minas Gerais, Brazil.</p>
<div class="card"><img src="sniff-and-sort.png" alt="Sniff & Sort icon"><div>
<h2>Sniff & Sort: Luggage Puzzle</h2>
<p>Every bag has a flight to catch. Clear the luggage jam, help the sniffer dog find the mystery bags and travel the world.</p>
<p class="langs"><a href="support.html">Support</a>
<a href="privacy.html">Privacy Policy</a>
<a href="privacidade.html">Política de Privacidade</a>
<a href="privacidad.html">Política de Privacidad</a>
<a href="delete-account.html">Delete account</a></p>
</div></div>"""
page("index.html", "Buriti Play", "en", index, NAV)
print("ok")

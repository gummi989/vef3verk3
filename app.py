from sys import argv
import bottle


@bottle.route("/")
def index():
    return """
    <h1>Verkefni 3</h1>
    <a href="/a">Liður a</a>
    <br>
    <a href="/b">Liður b</a>
    """


# 3a - Digit sum of SSN
@bottle.route("/a")
def index_a():
    return bottle.template("index_a.tpl")


@bottle.route("/a/ssn_digit_sum/<ssn>")
def ssn(ssn):
    return bottle.template("ssn.tpl", ssn=ssn)


@bottle.error(404)
def error404(error):
    return "<h1>Error 404: Page not found.</h1>"


# 3b - News
@bottle.route("/static/<filename:path>")
def static_file(filename):
    return bottle.static_file(filename, root="static")


stories = [
    ["Bjarni blandar sér í umræðuna",
     "Bjarni Benediktsson fjármálaráðherra blandaði sér í umræðuna í gærkvöld.",
     "bjarni.ben@hotmail.is"],
    ["Leitar réttar síns vegna uppsagnar",
     "Jónasi Í. Hvalnum var sagt upp störfum síðastliðinn föstudag. Síðan þá hefur hann leitað 1944 réttar síns án árangurs.",
     "jonas.i.hvalnum@yahoo.ru"],
    ["Töfrabragðið sem þrífur pönnuna á 20 mínútum",
     "Vísindamenn hafa uppgötvað leið til að þrífa pönnu á aðeins 20 mínútum. Þeir vilja þó ekki gefa út hvert það er.",
     "david.blaine@yandex.ru"],
    ["Snjókoma í kortunum",
     "Maður var að skoða póstkort á heimili sínu í gærkvöld þegar hann sá snjókomu á einu þeirra. Þessi frétt verður uppfærð.",
     "hingle.mccringleberry@foxnews.com"]
]


@bottle.route("/b")
def index_b():
    return bottle.template("index_b.tpl", stories=stories)


@bottle.route("/b/story/<id:int>")
def story(id):
    if id >= len(stories):
        bottle.abort(404)
    else:
        return bottle.template("story.tpl", story=stories[id], id=id)


bottle.run(host="0.0.0.0", port=argv[1], reloader=True, debug=True)

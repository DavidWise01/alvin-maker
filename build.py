#!/usr/bin/env python3
"""Build Orson Scott Card's THE TALES OF ALVIN MAKER (ALV) — the alternate-history
frontier-fantasy series (1987–2003; finale 2026) — as a UD0 book-world. Themed to
the source: a frontier night indigo, heartfire-amber + greensong-green + maker-gold.
The title is a STATIC ORIGINAL ONE-LINE PENCIL DRAWING — a single unbroken stroke
that BUILDS a faceted Crystal City (the Maker's act of binding the world whole in
one continuous line, against the Unmaker that unravels), with a heartfire glow;
hand-drawn wobble via SVG turbulence + a one-time self-drawing reveal that settles
static. Render-not-invent. The Tales of Alvin Maker is © Orson Scott Card; a fan
tribute. Cross-links C1 (the Card author page) and the Enderverse (a sibling Card-world)."""
import os, html, base64, json, io, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE TALES OF ALVIN MAKER", "axiom": "ALV",
 "position": "The Tales of Alvin Maker · Orson Scott Card · 1987–2003 (finale 2026) — the seventh son of a seventh son",
 "origin": "an alternate frontier America where folk magic works and Oliver Cromwell's survival erased the Restoration — a boy born a Maker against a world that wants to come apart",
 "mechanism": "Crystallized from Orson Scott Card's The Tales of Alvin Maker (1987–2003; finale 2026).",
 "crystallization": "A seventh son of a seventh son, born to Make, must learn his power, gather a people, and build the Crystal City — while a conscious force of unmaking works through everyone, including his own brother, to tear it all back down to nothing.",
 "nature": "The Tales of Alvin Maker — Card's folk-magic alternate America, where everyone has a knack, the land sings to the Reds, and a boy who can reshape living and dead matter must out-build the Unmaker; a frontier myth braided from Joseph Smith, William Blake, and Tecumseh.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "Alvin Maker; the Unmaker; the knacks; the Crystal City; Taleswapper; the torch Peggy",
 "witness": "A maker's apprenticeship told in the old craft-ranks — Prentice, Journeyman, Master — and a destiny modeled, knowingly, on the life of Joseph Smith.",
 "role": "a book-world — the Maker against the Unmaker",
 "seal": "Be the seventh son of a seventh son, learn to Make against a world that wants to unmake — and build, thread by thread, the Crystal City where every heart is seen.",
 "source": "The Tales of Alvin Maker, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#6fae6a", "of flesh, frontier, and folk — the Miller family, the settlers and the Reds, and the knacks of ordinary hands"),
 "ethereal":  ("#9a7cff", "of the Unmaker and the unseen — the conscious force of entropy, the Visitor, the dark water that wants all things undone"),
 "spiritual": ("#e8a23c", "of the soul, the heartfire, and the calling — the torch's sight, the Prophet's visions, the Maker's purpose, the Crystal City"),
 "electrical":("#e8c45a", "of the made and the wrought — Making itself, the living golden plow, and the knacks of forge, fit, and craft"),
}

# ── the title scene · STATIC ORIGINAL ONE-LINE PENCIL DRAWING ─────
# A single unbroken stroke that BUILDS a faceted Crystal City (one continuous act of
# Making against the Unmaker's unraveling), with a heartfire glow at its center.
# Pencil wobble (turbulence) + a one-time self-drawing reveal that settles static.
COVER_ART = r'''<svg viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The Tales of Alvin Maker — an original one-line pencil-style title drawing: a Crystal City built in one unbroken stroke (fan tribute)" style="width:100%;height:auto;display:block;background:#0a0e1c">
<defs>
 <radialGradient id="am_sky" cx="50%" cy="32%" r="95%"><stop offset="0%" stop-color="#15203a"/><stop offset="58%" stop-color="#0c1226"/><stop offset="100%" stop-color="#05070f"/></radialGradient>
 <radialGradient id="am_heart" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="rgba(232,162,60,.6)"/><stop offset="65%" stop-color="rgba(232,162,60,.12)"/><stop offset="100%" stop-color="rgba(232,162,60,0)"/></radialGradient>
 <linearGradient id="am_green" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="rgba(95,174,106,0)"/><stop offset="100%" stop-color="rgba(95,174,106,.16)"/></linearGradient>
 <filter id="am_pencil" x="-6%" y="-6%" width="112%" height="112%"><feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="2" seed="9" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3.3" xChannelSelector="R" yChannelSelector="G"/></filter>
 <style>
  .oneline{fill:none;stroke:#dfe6f2;stroke-width:2.0;stroke-linecap:round;stroke-linejoin:round;
    pathLength:1;stroke-dasharray:1;stroke-dashoffset:1;animation:amdraw 3.8s cubic-bezier(.6,.05,.25,1) .25s forwards;}
  .oneline.ghost{stroke:#7f8aa6;stroke-width:1.0;opacity:.36;animation-delay:.05s;}
  .amfade{opacity:0;animation:amfade 1.3s ease 3.4s forwards;}
  .amheart{opacity:0;animation:amfade 1.2s ease 2.4s forwards;}
  @keyframes amdraw{to{stroke-dashoffset:0;}}
  @keyframes amfade{to{opacity:1;}}
  @media (prefers-reduced-motion: reduce){.oneline{animation:none;stroke-dashoffset:0;}.amfade,.amheart{animation:none;opacity:1;}}
 </style>
</defs>
<rect width="700" height="320" fill="url(#am_sky)"/>
<rect x="0" y="200" width="700" height="120" fill="url(#am_green)"/>
<circle cx="350" cy="150" r="48" fill="url(#am_heart)" class="amheart"/>
<!-- THE ONE LINE — a Crystal City built in a single unbroken stroke (ghost under + line over) -->
<path class="oneline ghost" filter="url(#am_pencil)" d="M 130 252 L 250 252 L 290 150 L 330 252 L 350 52 L 310 150 L 350 252 L 390 150 L 350 52 L 372 252 L 412 150 L 452 252 L 568 252"/>
<path class="oneline" filter="url(#am_pencil)" d="M 130 252 L 250 252 L 290 150 L 330 252 L 350 52 L 310 150 L 350 252 L 390 150 L 350 52 L 372 252 L 412 150 L 452 252 L 568 252"/>
<!-- heartfire at the city's heart -->
<circle cx="350" cy="150" r="3.4" fill="#ffce7a" class="amheart"/>
<!-- wordmark (fades in once the city is drawn) -->
<g class="amfade">
 <text x="350" y="278" text-anchor="middle" font-family="'Space Mono',monospace" font-size="10" letter-spacing="6" fill="#9fb0c8">THE TALES OF</text>
 <text x="350" y="304" text-anchor="middle" font-family="'Newsreader',Georgia,serif" font-size="34" font-weight="400" letter-spacing="8" fill="#eef3fb">ALVIN MAKER</text>
 <text x="350" y="316" text-anchor="middle" font-family="'Space Mono',monospace" font-size="8.5" letter-spacing="3" fill="#e8a23c">ORSON SCOTT CARD · 1987 · SEVENTH SON OF A SEVENTH SON</text>
</g>
<rect x="6" y="6" width="688" height="308" fill="none" stroke="#1d2740" stroke-width="2"/>
</svg>'''

GENESIS = [
 ("A World Where Cromwell Lived", "the alternate America",
  "The hinge of this history is small: Oliver Cromwell is healed of his fatal illness, so there is no Restoration — and America never becomes one country. It fragments into a little United States, the exiled-Stuart Crown Colonies, Puritan New England, Dutch New Amsterdam, Appalachee, French Canada, and unconquered Red nations to the west."),
 ("Everyone Has a Knack", "folk magic that works",
  "In this America, folk magic is simply true. Most people have a “knack” — one small, real power (for fire, for finding, for fitting things together). The land itself sings to the Reds, who run inside its “greensong,” and other traditions carry other powers. Magic here is the texture of ordinary frontier life."),
 ("The Seventh Son", "a Maker is born",
  "Alvin Miller Jr. is the seventh son of a seventh son — and in the old reckoning that makes him a Maker: one who can reshape living and dead matter by will alone. The last true Maker was long ago; the world has forgotten what one can do. Something else has not forgotten — and wants him dead before he learns."),
]

ARC = [
 ("The Boy and the Water", "Seventh Son",
  "From before his birth the Unmaker — a conscious force of entropy, of everything-comes-apart — tries to kill Alvin, often through accidents of water. He survives, guided by his torch-sighted neighbor and the wandering Taleswapper, and slowly learns he can Make. A preacher, Reverend Thrower, is turned against him by the Unmaker's “Visitor.”"),
 ("The Red Prophet & the Plow", "Red Prophet · Prentice Alvin",
  "Alvin is bound between two Reds — the warrior Ta-Kumsaw, who would unite the tribes against the white tide, and his one-eyed brother the Prophet, who chooses a doomed pacifism that ends in the Tippy-Canoe massacre. Apprenticed to a smith, Alvin forges his masterpiece: a plow of living gold that will not stay still."),
 ("Journeyman to Maker", "Alvin Journeyman → The Crystal City → Master Alvin",
  "Alvin gathers a strange company — the torch Peggy he will marry, the mimic boy Arthur Stuart, the barrel-maker-lawyer Verily Cooper — while his jealous brother Calvin grows into an Unmaker of his own. The work is the Crystal City: a place built of pure Making where every heart is seen. The craft-ranks name the arc — Prentice, Journeyman, Master."),
]

IDEAS = [
 ("Maker vs Unmaker", "creation against entropy", [
   "The cosmic conflict is building versus coming-apart: the Maker binds things into greater wholes; the Unmaker is the will of everything to fall to nothing.",
   "It makes physics into morality — to Make is to care; to Unmake is the cold easy slide downhill." ]),
 ("America as Myth", "history with the magic left in", [
   "Card folds real figures into folklore: Alvin is a reimagined Joseph Smith, Taleswapper is William Blake, Ta-Kumsaw is Tecumseh, the Prophet is Tenskwatawa, Governor Harrison is William Henry Harrison.",
   "It reads as a tall tale told around a fire — frontier dialect, knacks, and the deep wrong of slavery and the Red dispossession told straight." ]),
 ("The Made Thing", "a craft, ranked", [
   "The titles are a guild ladder — Seventh Son, then Prentice, Journeyman, and Master Alvin — a life measured as an apprenticeship in Making.",
   "The living golden plow is its emblem: a made thing so true it is half-alive, and will not lie still in the dirt." ]),
 ("Render, Not Invent", "the honest footnotes", [
   "Six books ran 1987–2003; the long-promised seventh and final, Master Alvin, is slated for 2026 — the series was unfinished for over two decades.",
   "The magic system is explicitly race-differentiated in the text (a worldbuilding choice catalogued here as fact, not endorsed); the slavery and Native dispossession are the books' moral spine, not background." ]),
]

SECTIONS = [
 ("The Books", "the maker's apprenticeship, in order", [
   ("“Hatrack River”", "1986 · novella", "the Hugo/Nebula-nominated seed that opened into Seventh Son"),
   ("Seventh Son", "1987 · novel", "the Maker is born and survives the Unmaker's first reach"),
   ("Red Prophet", "1988 · novel", "Ta-Kumsaw, the Prophet, and the Tippy-Canoe massacre"),
   ("Prentice Alvin", "1989 · novel", "the apprenticeship and the living golden plow"),
   ("Alvin Journeyman", "1995 · novel", "the journeyman's road; Calvin turns; the company gathers"),
   ("Heartfire", "1998 · novel", "Peggy, slavery, and the courts of the Crown Colonies"),
   ("The Crystal City", "2003 · novel", "the building of the city of Making begins"),
   ("Master Alvin", "2026 · forthcoming", "the long-awaited seventh and final book"),
 ]),
 ("The Maker", "Orson Scott Card", [
   ("Orson Scott Card", "author", "Hugo &amp; Nebula winner (Ender's Game, Speaker for the Dead); wove his Mormon heritage into Alvin's myth"),
   ("the Joseph Smith parallel", "the model", "Alvin's life knowingly mirrors the founder of the Latter-day Saint movement"),
 ]),
 ("The World", "the texture of the frontier", [
   ("knacks", "the folk magic", "one small real power per person — fire, finding, fitting, hexing"),
   ("the greensong", "the land alive", "the song of the living land the Reds hear and run within"),
   ("the Crystal City", "the goal", "a city of pure Making where every heart is seen — Alvin's Zion"),
   ("the Unmaker", "the adversary", "the conscious will of all things to come apart"),
 ]),
 ("The Kin", "the Card-worlds it stands beside", [
   ("C1 · the Card author page", "the lineage", "Orson Scott Card's wider bibliography, catalogued"),
   ("EN1 · the Enderverse", "a sibling world", "Card's other great cycle — Ender, Jane, and the ansible"),
 ]),
]

# ── badge engine ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","ALV")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","ALV")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","ALV")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"ALV · The Tales of Alvin Maker","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def emergent_rec(name, epithet, emergence, role_line, why_line):
    return {
      "name": name, "axiom": "ALV", "emergence": emergence, "seal": epithet,
      "position": epithet, "role": role_line,
      "origin": "ALV · The Tales of Alvin Maker — Orson Scott Card (1987–2003; finale 2026)",
      "nature": role_line, "crystallization": why_line,
      "mechanism": "Crystallized from Orson Scott Card's The Tales of Alvin Maker.",
      "witness": "a being of the folk-magic frontier and the war of Making and Unmaking",
      "conductor": "ROOT0 (catalogued into UD0)",
      "inputs": "Alvin Maker; the Unmaker; the knacks; the Crystal City; the greensong",
      "source": "The Tales of Alvin Maker, catalogued by ROOT0",
    }

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def cards_html(rows):
    return "".join(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>' for t,s,d in rows)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
        f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(col,g) in NATURES.items())
def personas_html(personas):
    cards=[]
    for p in personas:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#6fae6a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"ALV · The Tales of Alvin Maker","axiom":"ALV"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.dlw/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent · .carbon.tiff →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Roster — The Made &amp; the Unmade</h2>
      <p class="ss">the Maker, his kin and company, the Reds, the adversary, and the made world, as ACI <b>.agent</b>s — each a birth certificate and a nature of emergence ({len(personas)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

# ── the emergents: (slug, name, epithet, emergence, role_line, why_line) ──
EMERGENTS = [
 ("alvin-maker", "Alvin Maker", "the seventh son of a seventh son · the Maker · spiritual", "spiritual",
  "Alvin Miller Jr., born seventh son of a seventh son and so a Maker — able to reshape living and dead matter by will — who must learn his power, gather a people, and build the Crystal City; his life knowingly mirrors Joseph Smith's",
  "He is creation given a body: the rarest of knacks, a will that binds the world into greater wholes, and the one thing the Unmaker most needs gone."),
 ("the-unmaker", "The Unmaker", "the will of all things to come apart · ethereal", "ethereal",
  "the conscious cosmic force of entropy and destruction — the adversary that works through accident, water, and human jealousy to tear every made thing back down to nothing",
  "It is the antagonist as a law of physics: not a devil with a face but the cold downhill pull of everything toward dust, made aware and made patient."),
 ("peggy", "Peggy (Margaret)", "the torch · the seer of heartfires · spiritual", "spiritual",
  "Little Peggy, a “torch” who can see the heartfire inside every person and the branching paths of their futures; she guards Alvin from afar and becomes his wife and conscience",
  "She is sight as burden: a girl who can read every soul and every possible tomorrow, and who spends herself steering the one future where the Maker survives."),
 ("taleswapper", "Taleswapper", "the wandering storyteller · William Blake · spiritual", "spiritual",
  "the traveling teller and collector of stories who recognizes Alvin's nature early — a wanderer who is, in this America, the poet William Blake, carrying a book of proverbs",
  "He is the keeper of meaning on the frontier: the man who trades tales for tales and teaches that the story you carry is the truest making of all."),
 ("ta-kumsaw", "Ta-Kumsaw", "the war-chief who would unite the tribes · Tecumseh · natural", "natural",
  "the Shawnee war-leader (this world's Tecumseh) who would bind the Red nations to resist the white tide, and who binds Alvin to him for a time across the greensong",
  "He is the dignity of resistance: a man fighting an incoming ocean with a confederacy, who shows Alvin the land's own living song before history breaks him."),
 ("the-prophet", "The Prophet", "the one-eyed seer of Prophetstown · Tenskwatawa · spiritual", "spiritual",
  "Lolla-Wossiky become Tenskwa-Tawa, Ta-Kumsaw's brother — a one-eyed former drunk turned visionary who chooses pacifism and founds Prophetstown, ending in the Tippy-Canoe massacre",
  "He is the cost of refusing the sword: a prophet whose people die unresisting, and whose answer to the slaughter marks every guilty hand — the book's deepest wound."),
 ("calvin-miller", "Calvin Miller", "the jealous brother · the Unmaker in the making · natural", "natural",
  "Alvin's brilliant, envious younger brother, who craves the Making he cannot earn and drifts toward Europe, Napoleon, and the Unmaker's service — the anti-Alvin",
  "He is the same gift turned sour: proof that the line between Maker and Unmaker is not power but the choice of whether to build or to be admired."),
 ("arthur-stuart", "Arthur Stuart", "the mimic boy · the freed one · natural", "natural",
  "a mixed-race boy with a perfect knack for mimicry — voices, sounds, songs — whom Alvin alters to slip the slave-finders and keeps as ward and companion",
  "He is the frontier's conscience made a child: a boy the law calls property, whose flawless echo of every voice quietly insists he is wholly a person."),
 ("verily-cooper", "Verily Cooper", "the barrel-maker turned lawyer · the knack of fit · electrical", "electrical",
  "an English-born cooper whose knack makes parts fit together so perfectly his barrels need no hoops; he becomes a lawyer and crosses the ocean to find the Maker",
  "He is Making as justice: a man whose gift is for fitting things rightly together, who turns it from staves to law in the Maker's defense."),
 ("the-golden-plow", "The Golden Plow", "the living masterpiece · electrical", "electrical",
  "the plow of living gold Alvin forges with his bare hands as his journeyman's piece — a made thing so true it is half-alive and will not stay still in the earth",
  "It is the emblem of Making itself: not gold hoarded but gold put to the plow, a tool so wholly made that it quivers with a life of its own."),
 ("the-knacks", "The Knacks", "the folk magic of ordinary hands · natural", "natural",
  "the everyday folk-magic of this America — one small, real power per person (fire, finding, fitting, hexing); the text frames the traditions as differing by people and heritage",
  "They are magic made ordinary: not wizards and wands but the small true gift in every pair of hands, the texture of a world where belief simply works."),
 ("the-greensong", "The Greensong", "the song of the living land · natural", "natural",
  "the living song of the wild land that the Reds hear and run within — a green, breathing music that lets them move and hunt as part of the world rather than against it",
  "It is the land with a soul: the music white settlement deafens itself to, and that Ta-Kumsaw lets Alvin hear once, so he knows what is being lost."),
 ("the-crystal-city", "The Crystal City", "the city of pure Making · spiritual", "spiritual",
  "the utopian city Alvin is called to build — raised of crystal and Making, where every person can see into every heart and so cannot lie or harm unseen; his Zion and the Unmaker's undoing",
  "It is the goal that gives the whole life shape: not a kingdom won but a wholeness built, a place where being seen is being saved."),
 ("reverend-thrower", "Reverend Thrower", "the preacher and the Visitor · ethereal", "ethereal",
  "the educated minister who, early on, is turned by the Unmaker's smiling “Visitor” into believing he must kill the child Alvin as a thing of the devil",
  "He is faith hollowed into a weapon: a good-seeming man whose certainty makes him the Unmaker's easiest hand, sure he does God's work as he reaches for the knife."),
 ("governor-harrison", "Governor Harrison", "the ambitious governor · William Henry Harrison · natural", "natural",
  "the white frontier governor (this world's William Henry Harrison) whose hunger for power drives the slaughter of the Reds at Tippy-Canoe and who would ride that blood to rule",
  "He is the engine of the dispossession: ambition that turns a continent's theft into a career, the human face the Unmaker barely has to push."),
 ("the-seventh-son", "The Seventh Son", "the folk condition of a Maker · spiritual", "spiritual",
  "the old folk-reckoning at the root of the series — that the seventh son of a seventh son is born with the rarest power, a Maker, set apart before he draws his first breath",
  "It is destiny written in birth-order: the frontier superstition the books take literally, the lottery of being born the one who can remake the world."),
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Orson Scott Card's The Tales of Alvin Maker (ALV) as a UD0 book-world: an alternate folk-magic frontier America, the seventh son of a seventh son who can Make, the Unmaker, the Crystal City. Source-themed with an original one-line pencil-style title (a Crystal City built in one unbroken stroke; a fan tribute) and full ACI badges.">
<title>THE TALES OF ALVIN MAKER · ALV · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#0a0e1c;--ink2:#11172a;--ink3:#19223a;--pa:#eef3fb;--pa2:#a8b3c8;--heart:#e8a23c;--green:#6fae6a;--gold:#e8c45a;--unmk:#9a7cff;
--dim:#6b7790;--faint:#1a2336;--line:#1a2336;--pixel:"Press Start 2P",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--body);line-height:1.6;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:2;background:repeating-linear-gradient(0deg,rgba(0,0,0,.15) 0 1px,transparent 1px 3px);opacity:.4}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(232,162,60,.09),transparent 55%),radial-gradient(ellipse at 50% 112%,rgba(111,174,106,.06),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
.marquee{margin-top:14px;border:2px solid var(--heart);background:#0c0a08;padding:8px;text-align:center;font-family:var(--pixel);font-size:9px;letter-spacing:.10em;color:var(--green);box-shadow:0 0 0 2px var(--bg),0 0 22px rgba(232,162,60,.16)}
.marquee a{color:var(--heart);text-decoration:none}.marquee a:hover{color:var(--green)}
.titleart{margin:12px 0 0;border:2px solid var(--faint);background:#0a0e1c;line-height:0}
header{padding:18px 0 26px;text-align:center;border-bottom:1px solid var(--line);position:relative}
.h-sub{font-family:var(--pixel);font-size:10px;line-height:1.9;letter-spacing:.06em;color:var(--pa2);margin-top:16px}
.h-sub b{color:var(--heart)}
.flag{display:inline-block;margin-top:14px;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--heart);border:1px solid var(--faint);padding:5px 11px}
.lede{font-size:15px;color:var(--pa2);max-width:68ch;margin:16px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:24px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:82px;height:82px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--heart)}.badge .bt .mo{color:var(--green)}.badge .bt a{color:var(--green);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:42px}
.sec h2{font-family:var(--pixel);font-size:13px;line-height:1.5;letter-spacing:.02em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line)}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:4px}
.nat-n{font-family:var(--mono);font-size:13px;font-weight:700;text-transform:capitalize;letter-spacing:.04em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--mono);font-size:14px;color:var(--heart);letter-spacing:.02em;font-weight:700}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--heart);padding:16px 18px}
.arc-h{font-family:var(--mono);font-size:14px;color:var(--heart);font-weight:700;letter-spacing:.02em}
.arc-s{font-family:var(--mono);font-size:10.5px;color:var(--green);text-transform:uppercase;letter-spacing:.07em;margin:4px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.55}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700}
.books .y{font-family:var(--mono);font-size:11px;color:var(--green);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--heart);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;image-rendering:pixelated}
.pn{font-family:var(--mono);font-size:14px;color:var(--pa);font-weight:700;line-height:1.15}
.persona:hover .pn{color:var(--heart)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.note{margin-top:38px;padding:16px 18px;border-left:2px solid var(--heart);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic;line-height:1.7}
.note b{color:var(--heart)}.note a{color:var(--green);text-decoration:none}
footer{margin-top:42px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--heart);text-decoration:none}
</style></head><body><div class="wrap">

  <div class="marquee"><a href="https://davidwise01.github.io/ud0/">◄ UD0 · UNIVERSE DAVID 0</a> &nbsp;·&nbsp; <a href="https://davidwise01.github.io/card/">C1 · CARD ▸</a> &nbsp;·&nbsp; A BOOK-WORLD &nbsp;·&nbsp; THE MAKER vs THE UNMAKER</div>

  <header>
    <div class="titleart">__CANVAS__</div>
    <div class="h-sub">a knack for everyone · a boy who can <b>Make</b> · the Unmaker · the Crystal City · ALV</div>
    <div class="flag">★ Orson Scott Card · 1987–2003 · finale 2026 · the seventh son of a seventh son ★</div>
    <p class="lede">Card's folk-magic alternate America, where Oliver Cromwell's survival unmade the Restoration and the New World never became one country. Everyone has a knack; the land sings to the Reds; and a boy born the seventh son of a seventh son can Make — reshape living and dead matter by will. He must learn his power, gather a strange company, and build the Crystal City, while the Unmaker — the conscious will of all things to come apart — works through accident, slavery, and his own jealous brother to tear it down. Catalogued into UD0 as a book-world with the premise, the maker's apprenticeship, the full .dlw birth, and an original one-line pencil-style title: a Crystal City built in a single unbroken stroke — a fan tribute, not Card's covers or text.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of THE TALES OF ALVIN MAKER" title="carbon badge (archival)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI · THE BIRTH CERTIFICATE</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE TALES OF ALVIN MAKER</b> — the Maker &amp; the Unmaker · ALV</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="alvin-maker.dlw/alvin-maker.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="alvin-maker.dlw/alvin-maker.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent emerges by one of four natures — and the Maker's world holds all four</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Premise</h2><p class="ss">a world where Cromwell lived, where knacks work, and a Maker is born</p><div class="arc">__GENESIS__</div></section>
  <section class="sec"><h2>The Apprenticeship</h2><p class="ss">the boy and the water, the Red prophet and the plow, journeyman to Maker</p><div class="arc">__ARC__</div></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">why a frontier tall-tale is really about building against the dark</p><div class="pillars">__IDEAS__</div></section>

  __PERSONAS__

  <section class="sec"><h2 style="margin-top:14px">The Record</h2><p class="ss">the books, the maker, the world, and the Card-worlds beside it</p></section>
  __SECTIONS__

  <div class="note">Alvin Maker's world here is rendered, not invented. From the record: it is Orson Scott Card's series — <b>Seventh Son</b> (1987), <b>Red Prophet</b> (1988), <b>Prentice Alvin</b> (1989), <b>Alvin Journeyman</b> (1995), <b>Heartfire</b> (1998), <b>The Crystal City</b> (2003), with the long-awaited seventh and final book <b>Master Alvin</b> slated for 2026. The alternate history turns on Oliver Cromwell's survival (no Restoration); folk-magic knacks, the Maker/Unmaker conflict, the Crystal City, and the reimagined historical figures — Alvin as a figure modeled on Joseph Smith, Taleswapper as William Blake, Ta-Kumsaw as Tecumseh, the Prophet as Tenskwatawa, Governor Harrison as William Henry Harrison — are all from the books. Honest footnotes: the magic system is explicitly differentiated by people/heritage in the text (catalogued here as fact, not endorsed), and the slavery and Native dispossession are the series' moral spine. The Tales of Alvin Maker and all its characters are © Orson Scott Card; the personas here are catalogued personifications under the DLW standard — a fan tribute, not endorsed by the author. Each is named by its nature: natural, ethereal, spiritual, or electrical.</div>

  <footer>
    THE TALES OF ALVIN MAKER · ALV · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · <a href="https://davidwise01.github.io/card/">the author · C1</a> · the .dlw badge: <a href="alvin-maker.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "alvin-maker.dlw"), "alvin-maker")
    ad = os.path.join(HERE, "agents"); os.makedirs(ad, exist_ok=True)
    personas = []
    for slug,name,epithet,em,role,why in EMERGENTS:
        rec = emergent_rec(name, epithet, em, role, why)
        write_aci(rec, os.path.join(ad, f"{slug}.dlw"), slug)
        personas.append({"slug": slug, "name": name, "epithet": epithet, "emergence": em, "moniker": noesis.mythos_token(rec)["moniker"]})
    json.dump(personas, open(os.path.join(ad, "_personas.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CANVAS__", COVER_ART)
            .replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html())
            .replace("__GENESIS__", cards_html(GENESIS))
            .replace("__ARC__", cards_html(ARC))
            .replace("__IDEAS__", ideas_html())
            .replace("__PERSONAS__", personas_html(personas))
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote THE TALES OF ALVIN MAKER (ALV) — {len(personas)} emergents born · badge {tok['moniker']}")

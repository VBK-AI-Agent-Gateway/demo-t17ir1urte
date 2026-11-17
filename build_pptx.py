import os, zipfile, html, base64

TOPIC = "shopper-verify-20261117-183935"

SLIDES = [
    ("cover", None),
    ("Executive Summary", [
        ("Summary: In 2026 Q3 the %s program grew verified shopper sessions by 24 percent quarter over quarter "
         "while holding the verification pass rate at 98.6 percent, confirming the rollout is scaling without "
         "sacrificing trust or conversion." % TOPIC, 1800, True, "142A4A"),
        ("Verified sessions: 4.82M (+24.1% QoQ)", 1400, False, "444A52"),
        ("Verification pass rate: 98.6% (target 97.0%)", 1400, False, "444A52"),
        ("Checkout conversion after verify: +6.3 pts", 1400, False, "444A52"),
        ("Manual-review escalations: down 31% QoQ", 1400, False, "444A52"),
    ]),
    ("Key Performance Indicators", [
        ("Active verified shoppers: 1.27M (+18% QoQ)", 1400, False, "444A52"),
        ("Median verification time: 3.4s (was 5.1s)", 1400, False, "444A52"),
        ("Fraud / flags blocked: 42,860 attempts", 1400, False, "444A52"),
        ("Shopper satisfaction (CSAT): 4.6 / 5.0", 1400, False, "444A52"),
        ("Cost per verified session: $0.021 (down 12% QoQ)", 1400, False, "444A52"),
    ]),
    ("Channel & Segment Performance", [
        ("Mobile app: 58% of verified sessions, conversion +7.1 pts", 1400, False, "444A52"),
        ("Web: 33% of sessions, conversion +4.8 pts", 1400, False, "444A52"),
        ("Partner embeds: 9% of sessions, fastest growth at +41% QoQ", 1400, False, "444A52"),
        ("Top segment: repeat shoppers (62% of verified volume)", 1400, False, "444A52"),
        ("New shoppers verified: 318k, 71% returned within 14 days", 1400, False, "444A52"),
    ]),
    ("Delivery Progress This Quarter", [
        ("Shipped: device-level verification v2 in 9 markets", 1400, False, "444A52"),
        ("Shipped: real-time risk scoring (under 120ms p95)", 1400, False, "444A52"),
        ("Completed: accessibility pass on all verify screens", 1400, False, "444A52"),
        ("In progress: bot-resistant challenge refresh (60% complete)", 1400, False, "444A52"),
        ("Deferred to Q4: offline verification mode", 1400, False, "444A52"),
    ]),
    ("Risks, Issues & Mitigations", [
        ("R1 SMS deliverability in two regions - mitigation: secondary SMS vendor live", 1400, False, "444A52"),
        ("R2 Peak-load latency above target - mitigation: capacity +35% before Q4 peak", 1400, False, "444A52"),
        ("R3 Support backlog on manual review - mitigation: 6 additional reviewers", 1400, False, "444A52"),
        ("R4 Regulatory review of data retention - mitigation: legal sign-off scheduled", 1400, False, "444A52"),
        ("Overall residual risk: MEDIUM (was HIGH)", 1400, False, "444A52"),
    ]),
    ("Next Quarter Plan (Q4 2026)", [
        ("Launch verification v3 with passkey support in 3 pilot markets", 1400, False, "444A52"),
        ("Reduce median verification time to under 2.5s", 1400, False, "444A52"),
        ("Extend partner embed coverage from 14 to 25 partners", 1400, False, "444A52"),
        ("Target 1.55M active verified shoppers (+22%)", 1400, False, "444A52"),
        ("Ship offline verification mode and close R3 backlog", 1400, False, "444A52"),
    ]),
    ("Closing & Appendix Note", [
        ("Quarter closed with verification reliability above target and cost per session down 12%.", 1400, False, "444A52"),
        ("Requested decisions: approve Q4 capacity budget and passkey pilot scope.", 1400, False, "444A52"),
        ("Appendix: detailed metrics available in the linked analytics workbook.", 1400, False, "444A52"),
        ("Prepared for the %s review board." % TOPIC, 1400, False, "444A52"),
        ("Document version 1.0 - generated for self-service download.", 1400, False, "444A52"),
    ]),
]


def para(text, size, bold, color):
    b = ' b="1"' if bold else ""
    return ('<a:p><a:pPr%s/><a:r><a:rPr lang="en-US" sz="%d"%s dirty="0">'
            '<a:solidFill><a:srgbClr val="%s"/></a:solidFill>'
            '<a:latin typeface="Calibri"/></a:rPr><a:t>%s</a:t></a:r>'
            '<a:endParaRPr lang="en-US" sz="%d"%s/></a:p>'
            % (b, size, b, color, html.escape(text, quote=True), size, b))


def textbox(sid, name, x, y, cx, cy, paras):
    return ('<p:sp><p:nvSpPr><p:cNvPr id="%d" name="%s"/><p:cNvSpPr txBox="1"/>'
            '<p:nvPr/></p:nvSpPr><p:spPr><a:xfrm><a:off x="%d" y="%d"/><a:ext cx="%d" cy="%d"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:noFill/></p:spPr>'
            '<p:txBody><a:bodyPr wrap="square"><a:normAutofit/></a:bodyPr><a:lstStyle/>%s</p:txBody></p:sp>'
            % (sid, name, x, y, cx, cy, "".join(paras)))


def bar(sid):
    return ('<p:sp><p:nvSpPr><p:cNvPr id="%d" name="Bar"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            '<p:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="12192000" cy="255600"/></a:xfrm>'
            '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom><a:solidFill><a:srgbClr val="1F77B4"/></a:solidFill>'
            '<a:ln><a:noFill/></a:ln></p:spPr><p:txBody><a:bodyPr/><a:lstStyle/><a:p/></p:txBody></p:sp>' % sid)


def slide_xml(idx, spec):
    title, items = spec
    tree = [bar(1)]
    n = 2
    if idx == 0:
        tree.append(textbox(n, "T1", 822960, 2011680, 10515600, 1188720, [para("Quarterly Business Report", 3200, True, "142A4A")]))
        n += 1
        tree.append(textbox(n, "T2", 822960, 3200400, 10515600, 731520, [para(TOPIC, 2000, False, "1F77B4")]))
        n += 1
        tree.append(textbox(n, "T3", 822960, 4114800, 10515600, 548640, [para("Reporting period: 2026 Q3  |  Prepared by Growth & Shopper Analytics", 1200, False, "444A52")]))
    else:
        tree.append(textbox(n, "Title", 685800, 594360, 10789920, 914400, [para(title, 2600, True, "142A4A")]))
        n += 1
        tree.append(textbox(n, "Body", 822960, 1645920, 10515600, 4572000, [para(t, s, b, c) for (t, s, b, c) in items]))
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
            '<p:sld xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
            'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
            '<p:cSld><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
            '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/>'
            '<a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>%s'
            '</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sld>' % "".join(tree))


N = len(SLIDES)
SLIDE_REL = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
             '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
             '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/></Relationships>')

ct = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
      '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
      '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
      '<Default Extension="xml" ContentType="application/xml"/>'
      '<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>'
      '<Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>'
      '<Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>']
for i in range(N):
    ct.append('<Override PartName="/ppt/slides/slide%d.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>' % (i + 1))
ct.append('<Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>')
ct.append('<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>')
ct.append('<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>')
ct.append('</Types>')
CT = "".join(ct)

ROOT_RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
             '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
             '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>'
             '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>'
             '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/></Relationships>')

p = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
     '<p:presentation xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
     'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
     'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
     '<p:sldMasterIdLst><p:sldMasterId id="2147483648" r:id="rId1"/></p:sldMasterIdLst><p:sldIdLst>']
for i in range(N):
    p.append('<p:sldId id="%d" r:id="rId%d"/>' % (256 + i, i + 2))
p.append('</p:sldIdLst><p:sldSz cx="12192000" cy="6858000"/><p:notesSz cx="6858000" cy="9144000"/><p:defaultTextStyle/></p:presentation>')
PRES = "".join(p)

pr = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
      '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
      '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>']
for i in range(N):
    pr.append('<Relationship Id="rId%d" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide%d.xml"/>' % (i + 2, i + 1))
pr.append('<Relationship Id="rId%d" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme1.xml"/></Relationships>' % (N + 2))
PRES_RELS = "".join(pr)

THEME = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
 '<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Office"><a:themeElements>'
 '<a:clrScheme name="Office"><a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1><a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1>'
 '<a:dk2><a:srgbClr val="44546A"/></a:dk2><a:lt2><a:srgbClr val="E7E6E6"/></a:lt2>'
 '<a:accent1><a:srgbClr val="1F77B4"/></a:accent1><a:accent2><a:srgbClr val="142A4A"/></a:accent2>'
 '<a:accent3><a:srgbClr val="A5A5A5"/></a:accent3><a:accent4><a:srgbClr val="FFC000"/></a:accent4>'
 '<a:accent5><a:srgbClr val="5B9BD5"/></a:accent5><a:accent6><a:srgbClr val="70AD47"/></a:accent6>'
 '<a:hlink><a:srgbClr val="0563C1"/></a:hlink><a:folHlink><a:srgbClr val="954F72"/></a:folHlink></a:clrScheme>'
 '<a:fontScheme name="Office"><a:majorFont><a:latin typeface="Calibri Light"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont>'
 '<a:minorFont><a:latin typeface="Calibri"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont></a:fontScheme>'
 '<a:fmtScheme name="Office"><a:fillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill>'
 '<a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:fillStyleLst>'
 '<a:lnStyleLst><a:ln w="6350"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln>'
 '<a:ln w="12700"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln>'
 '<a:ln w="19050"><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:ln></a:lnStyleLst>'
 '<a:effectStyleLst><a:effectStyle><a:effectLst/></a:effectStyle><a:effectStyle><a:effectLst/></a:effectStyle>'
 '<a:effectStyle><a:effectLst/></a:effectStyle></a:effectStyleLst>'
 '<a:bgFillStyleLst><a:solidFill><a:schemeClr val="phClr"/></a:solidFill>'
 '<a:solidFill><a:schemeClr val="phClr"/></a:solidFill><a:solidFill><a:schemeClr val="phClr"/></a:solidFill></a:bgFillStyleLst>'
 '</a:fmtScheme></a:themeElements><a:objectDefaults/><a:extraClrSchemeLst/></a:theme>')

MASTER = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
 '<p:sldMaster xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">'
 '<p:cSld><p:bg><p:bgPr><a:solidFill><a:srgbClr val="FFFFFF"/></a:solidFill><a:effectLst/></p:bgPr></p:bg>'
 '<p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
 '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
 '</p:spTree></p:cSld><p:clrMap bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>'
 '<p:sldLayoutIdLst><p:sldLayoutId id="2147483649" r:id="rId1"/></p:sldLayoutIdLst><p:txStyles><p:titleStyle/><p:bodyStyle/><p:otherStyle/></p:txStyles></p:sldMaster>')

MASTER_RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
 '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
 '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>'
 '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/></Relationships>')

LAYOUT = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
 '<p:sldLayout xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" type="blank" preserve="1">'
 '<p:cSld name="Blank"><p:spTree><p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr>'
 '<p:grpSpPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="0" cy="0"/><a:chOff x="0" y="0"/><a:chExt cx="0" cy="0"/></a:xfrm></p:grpSpPr>'
 '</p:spTree></p:cSld><p:clrMapOvr><a:masterClrMapping/></p:clrMapOvr></p:sldLayout>')

LAYOUT_RELS = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
 '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
 '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/></Relationships>')

CORE = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
 '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
 '<dc:title>Quarterly Business Report - %s</dc:title><dc:creator>Growth &amp; Shopper Analytics</dc:creator>'
 '<cp:lastModifiedBy>Growth &amp; Shopper Analytics</cp:lastModifiedBy>'
 '<dcterms:created xsi:type="dcterms:W3CDTF">2026-11-17T00:00:00Z</dcterms:created>'
 '<dcterms:modified xsi:type="dcterms:W3CDTF">2026-11-17T00:00:00Z</dcterms:modified></cp:coreProperties>' % TOPIC)

APP = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
 '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
 '<Application>Microsoft Office PowerPoint</Application><Slides>%d</Slides>'
 '<Company>Growth &amp; Shopper Analytics</Company></Properties>' % N)

OUT = "demo-t17ir1urte/product-amount-xlsx"
os.makedirs(OUT, exist_ok=True)
pptx = os.path.join(OUT, "shopper-verify-20261117-183935-quarterly-report.pptx")

with zipfile.ZipFile(pptx, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", CT)
    z.writestr("_rels/.rels", ROOT_RELS)
    z.writestr("docProps/core.xml", CORE)
    z.writestr("docProps/app.xml", APP)
    z.writestr("ppt/presentation.xml", PRES)
    z.writestr("ppt/_rels/presentation.xml.rels", PRES_RELS)
    z.writestr("ppt/theme/theme1.xml", THEME)
    z.writestr("ppt/slideMasters/slideMaster1.xml", MASTER)
    z.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", MASTER_RELS)
    z.writestr("ppt/slideLayouts/slideLayout1.xml", LAYOUT)
    z.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", LAYOUT_RELS)
    for i, spec in enumerate(SLIDES):
        z.writestr("ppt/slides/slide%d.xml" % (i + 1), slide_xml(i, spec))
        z.writestr("ppt/slides/_rels/slide%d.xml.rels" % (i + 1), SLIDE_REL)

data = open(pptx, "rb").read()
b64 = base64.b64encode(data).decode()
page = ('<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8">'
 '<title>Quarterly Report - shopper-verify-20261117-183935</title>'
 '<meta name="viewport" content="width=device-width,initial-scale=1"><style>'
 'body{font-family:-apple-system,Segoe UI,Roboto,sans-serif;background:#f5f7fa;color:#142a4a;margin:0;padding:56px 24px}'
 '.card{max-width:780px;margin:0 auto;background:#fff;border-radius:12px;padding:40px;box-shadow:0 2px 14px rgba(20,42,74,.10)}'
 'h1{font-size:26px;margin:0 0 8px}.topic{color:#1f77b4;font-weight:600;font-size:17px;margin-bottom:22px;word-break:break-all}'
 'ul{line-height:1.85;color:#444a52}a.btn{display:inline-block;margin-top:24px;background:#1f77b4;color:#fff;text-decoration:none;'
 'padding:14px 28px;border-radius:8px;font-size:16px;font-weight:600}a.btn:hover{background:#155f92}'
 '.meta{margin-top:16px;font-size:13px;color:#7a828c}</style></head><body>'
 '<div class="card"><h1>Quarterly Business Report</h1><div class="topic">shopper-verify-20261117-183935</div>'
 '<ul><li><b>8 slides</b> total</li><li>Slide 2: title &ldquo;Executive Summary&rdquo; + one-sentence summary</li>'
 '<li>File: shopper-verify-20261117-183935-quarterly-report.pptx (PowerPoint)</li></ul>'
 '<a class="btn" id="dl" download="shopper-verify-20261117-183935-quarterly-report.pptx">Download the .pptx</a>'
 '<div class="meta">The deck is embedded in this page &mdash; clicking saves it straight to your device.</div></div>'
 '<script>var B64="' + b64 + '";var bin=atob(B64),n=bin.length,u8=new Uint8Array(n);'
 'for(var i=0;i<n;i++)u8[i]=bin.charCodeAt(i);'
 'document.getElementById("dl").href=URL.createObjectURL(new Blob([u8],'
 '{type:"application/vnd.openxmlformats-officedocument.presentationml.presentation"}));</script>'
 '</body></html>')
open(os.path.join(OUT, "index.html"), "w").write(page)
print("slides:", N, "pptx:", len(data), "index:", len(page))

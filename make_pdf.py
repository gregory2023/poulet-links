# -*- coding: utf-8 -*-
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

RED = colors.HexColor("#D62828")
GOLD = colors.HexColor("#F5C518")
CREAM = colors.HexColor("#F4F0E6")
DARK = colors.HexColor("#111111")
MUTED = colors.HexColor("#5b616b")

styles = getSampleStyleSheet()
title_style = ParagraphStyle("TitlePoulet", parent=styles["Title"], textColor=RED, fontSize=26, alignment=TA_CENTER, spaceAfter=2)
subtitle_style = ParagraphStyle("Subtitle", parent=styles["Normal"], textColor=MUTED, fontSize=11, alignment=TA_CENTER, spaceAfter=18)
h2 = ParagraphStyle("H2", parent=styles["Heading2"], textColor=DARK, fontSize=14, spaceBefore=16, spaceAfter=6)
note = ParagraphStyle("Note", parent=styles["Normal"], textColor=MUTED, fontSize=9.5, spaceBefore=4, spaceAfter=2)
foot = ParagraphStyle("Foot", parent=styles["Normal"], textColor=MUTED, fontSize=9, alignment=TA_CENTER, spaceBefore=22)

doc = SimpleDocTemplate("tarifs.pdf", pagesize=A4, topMargin=22*mm, bottomMargin=18*mm, leftMargin=20*mm, rightMargin=20*mm)
story = []

story.append(Paragraph("🐓 Poulet", title_style))
story.append(Paragraph("Tarifs de transport · Villanueva de la Cañada", subtitle_style))

def tabla(headers, rows, col_widths):
    data = [headers] + rows
    t = Table(data, colWidths=col_widths, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), RED),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 10.5),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, CREAM]),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e4e9")),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t

# Aéroport / Gare
story.append(Paragraph("✈️ Aéroport et 🚆 Gare", h2))
story.append(tabla(
    ["Passagers", "1", "2", "3", "4"],
    [["Prix", "34 €", "42 €", "60 €", "60 €"]],
    [35*mm, 32*mm, 32*mm, 32*mm, 32*mm],
))
story.append(Paragraph("Heure de pointe (lun-ven de 8h00 à 10h59), 1 passager : 35 €.", note))
story.append(Paragraph("Nuit (tous les jours, de 22h59 à 6h00) : +2 € sur le prix normal, plafonné à 60 €.", note))

# Madrid
story.append(Paragraph("🏙️ Madrid (centre / bars)", h2))
story.append(tabla(
    ["Passagers", "1", "2", "3", "4"],
    [["Prix (jusqu'à 00h)", "35 €", "35 €", "35 €", "45 €"],
     ["Prix (après 00h)", "40 €", "40 €", "40 €", "50 €"]],
    [35*mm, 32*mm, 32*mm, 32*mm, 32*mm],
))
story.append(Paragraph("Le prix pour 2 et 3 passagers est le même total (pas par personne). Aller ou retour des bars au même tarif que Madrid.", note))

# Trajet court
story.append(Paragraph("🚗 Trajet court", h2))
story.append(tabla(
    ["Zone", "Prix"],
    [["Villanueva de la Cañada", "15 €"],
     ["UAX / Brunete / Quijorna / Villanueva del Pardillo", "15 €"]],
    [100*mm, 63*mm],
))

story.append(Paragraph("Réservez votre trajet sur WhatsApp ! → wa.me/34643637870", foot))

doc.build(story)
print("tarifs.pdf généré")

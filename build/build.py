#!/usr/bin/env python3
"""Generates the static Pensero Ltd site into ../site. Plain HTML output, no runtime dependencies."""
import os, html
OUT = os.path.join(os.path.dirname(__file__), "..", "site")

def ph(label):
    return f'<span class="ph">[PLACEHOLDER: {html.escape(label)}]</span>'

EMAIL_HREF = "mailto:eddy@pensero.com"
EMAIL = f'<a href="{EMAIL_HREF}">eddy@pensero.com</a>'
REGNO = "HE 421465"
ADDRESS = "Agias Vryainis 12, Plot 495, 8560 Pegeia, Paphos, Cyprus"

NAV = [("index.html","Home"),("consulting.html","Consulting"),("software.html","Software"),
       ("about.html","About"),("contact.html","Contact")]

APPS = [
 ("inventory-forecast-tool.html","Inventory Forecast Tool"),
 ("launch-command-center.html","Launch Command Center"),
 ("sales-performance-dashboard.html","Sales Performance Dashboard"),
 ("voice-of-customer-dashboard.html","Voice of Customer Dashboard"),
]

def page(fname, title, desc, body, active):
    nav = "\n".join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h==active else ""}>{t}</a></li>' for h,t in NAV)
    full_title = "Pensero Ltd" if fname=="index.html" else f"{title} | Pensero Ltd"
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap">
<a class="brand" href="index.html">Pensero <span>Ltd</span></a>
<nav class="nav" aria-label="Main">
<ul>
{nav}
</ul>
</nav>
</div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
<div class="wrap">
<p>&copy; 2026 Pensero Ltd &middot; Registered in Cyprus &middot; Reg. No. {REGNO}</p>
<ul>
<li><a href="legal-notice.html">Legal Notice</a></li>
<li><a href="privacy.html">Privacy</a></li>
</ul>
</div>
</footer>
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(doc)

def head(eyebrow, h1, lead=""):
    lp = f"<p>{lead}</p>" if lead else ""
    return f'<section class="page-head"><div class="wrap"><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1>{lp}</div></section>'

# ---------------- Home ----------------
apps_short = {
 "inventory-forecast-tool.html":"Inventory reconciliation, demand forecasting and replenishment planning across Amazon FBA, Amazon AWD and third-party warehouses.",
 "launch-command-center.html":"A single cockpit for product launches and advertising: sales, PPC, rankings and inventory in one place.",
 "sales-performance-dashboard.html":"Business intelligence for Amazon sales: full-funnel metrics, growth analytics and a complete P&amp;L down to each fee line.",
 "voice-of-customer-dashboard.html":"Consolidates returns, refunds, customer comments and reviews to identify and track product and listing issues.",
}
home = f"""
<section class="hero"><div class="wrap">
<p class="eyebrow">Pensero Ltd &middot; Cyprus</p>
<h1>Consulting and software for Amazon e-commerce operations</h1>
<p class="lead">Pensero Ltd is a Cyprus company that advises businesses selling on Amazon and develops proprietary software applications for e-commerce operations.</p>
</div></section>
<section class="section"><div class="wrap">
<div class="grid grid-2">
<div class="card">
<h2>Consulting</h2>
<p>Operational and commercial advisory for Amazon businesses: product selection and development, listings, advertising and launches, inventory and logistics, controlling and financial analysis, organisation and processes.</p>
<p><a class="more" href="consulting.html">Consulting services</a></p>
</div>
<div class="card">
<h2>Software</h2>
<p>Pensero Ltd has developed four software applications covering inventory planning, product launches and advertising, sales reporting and customer feedback analysis. The software is licensed to business customers under licence agreements.</p>
<p><a class="more" href="software.html">Software overview</a></p>
</div>
</div>
</div></section>
<section class="section"><div class="wrap">
<h2 style="margin-top:0">Software applications</h2>
<div class="grid">
{''.join(f'<div class="card"><h3>{t}</h3><p>{apps_short[h]}</p><p><a class="more" href="{h}">Details</a></p></div>' for h,t in APPS)}
</div>
</div></section>
"""
page("index.html","Home","Pensero Ltd, Cyprus: consulting and software for Amazon e-commerce operations.",home,"index.html")

# ---------------- Consulting ----------------
areas = [
 ("Product selection and development",
  "Assessment of product opportunities and support in bringing products to market.",
  ["Product selection","Product development","Competitor and market analysis","Keyword research and reverse ASIN research"]),
 ("Listings and content",
  "Preparation and optimisation of product listings in Amazon Seller Central.",
  ["Listing optimisation (search relevance) for titles, bullet points and descriptions","Enhanced Brand Content and A+ Content","Listing flat-file creation and uploads to Seller Central","Product inserts"]),
 ("Advertising and product launches",
  "Planning and management of advertising and of the launch phase of new products.",
  ["Pay-per-click advertising management: Sponsored Products, Sponsored Brands, Sponsored Display, DSP and video","Product launches","Organic keyword rank tracking","Split testing and optimisation"]),
 ("Inventory, logistics and Seller Central operations",
  "Operational management of stock, inbound logistics and FBA processes.",
  ["Inventory management and logistics","Seller Central, FBA and logistics management"]),
 ("Controlling and financial analysis",
  "Financial transparency at product and business level as a basis for decisions.",
  ["Controlling","Cost of goods calculations","Financial analysis","Profitability analysis and margin improvement","Business reporting"]),
 ("Organisation and processes",
  "Structuring of teams, responsibilities and recurring workflows in Amazon businesses.",
  ["Organisational structure","Process design and documentation"]),
]
cons = head("Consulting","Consulting services",
 "Pensero Ltd advises businesses selling on Amazon marketplaces on operational, commercial and financial matters. The services are grouped into the following areas.")
cons += '<section class="section"><div class="wrap"><div class="grid grid-2">'
for t,d,items in areas:
    cons += f'<div class="card"><h2>{t}</h2><p>{d}</p><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"
cons += '</div></div></section>'
page("consulting.html","Consulting","Consulting services of Pensero Ltd for Amazon e-commerce businesses.",cons,"consulting.html")

# ---------------- Software overview ----------------
sw = head("Software","Software applications",
 "Pensero Ltd has developed and owns the following four software applications for Amazon e-commerce operations. The software is licensed to business customers under licence agreements.")
sw += '<section class="section"><div class="wrap"><div class="grid grid-2">'
for h,t in APPS:
    sw += f'<div class="card"><h2>{t}</h2><p>{apps_short[h]}</p><p><a class="more" href="{h}">Application details</a></p></div>'
sw += '</div>'
sw += """<h2>Common characteristics</h2>
<ul>
<li>Web applications developed by Pensero Ltd.</li>
<li>Built on cloud infrastructure (Google Cloud, BigQuery, PostgreSQL/Supabase) with automated data pipelines.</li>
<li>Integration with Amazon interfaces (Selling Partner API, Amazon Ads API, Brand Analytics) and further e-commerce systems.</li>
<li>Access restricted to authorised users of the licensee.</li>
</ul>
<p>Enquiries regarding the software can be addressed to Pensero Ltd via the <a href="contact.html">contact page</a>.</p>
</div></section>"""
page("software.html","Software","Software applications developed by Pensero Ltd: Inventory Forecast Tool, Launch Command Center, Sales Performance Dashboard, Voice of Customer Dashboard.",sw,"software.html")

# ---------------- App pages ----------------
def app_page(fname, name, summary, description, functions, tech, scale, status):
    b = head("Software", name, summary)
    b += '<section class="section"><div class="wrap narrow">'
    b += "<h2 style=\"margin-top:0\">Description</h2>" + "".join(f"<p>{p}</p>" for p in description)
    b += '<h2>Core functions</h2><ul class="feature-list">' + "".join(f"<li><strong>{a}:</strong> {c}</li>" for a,c in functions) + "</ul>"
    b += '<h2>Technology</h2><table class="facts"><tbody>' + "".join(f"<tr><th scope=\"row\">{a}</th><td>{c}</td></tr>" for a,c in tech) + "</tbody></table>"
    if scale:
        b += f"<h2>Scope of use</h2><p>{scale}</p>"
    b += f'<p class="status">{status}</p>'
    b += '<p>The software is licensed to business customers under licence agreements.</p>'
    b += '<a class="backlink" href="software.html">&larr; All software applications</a></div></section>'
    page(fname, name, summary, b, "software.html")

app_page("inventory-forecast-tool.html","Inventory Forecast Tool",
 "Demand forecasting and inventory planning for multi-marketplace e-commerce operations.",
 ["A web application that consolidates inventory data from Amazon FBA, Amazon AWD, third-party warehouses and the operator&rsquo;s own purchase-order system into a single reconciled stock position, and derives demand forecasts, reorder dates, order quantities and stockout risk from it."],
 [("Inventory reconciliation","an in-transit ledger across four booking systems that identifies stock not recorded in any of them."),
  ("Demand forecasting","monthly forecasts per SKU and marketplace, based on the prior-year seasonal shape scaled to the current sales level, with a fallback method where prior-year data is unreliable."),
  ("Replenishment planning","reorder dates and order quantities derived from per-supplier lead times, factory-holiday calendars and a day-by-day stock simulation."),
  ("Stockout risk analysis","per-shipment simulation across split deliveries, including the maximum sustainable daily sales rate until each arrival."),
  ("Exception management","threshold-gated alerts for forecast deviation, over- and under-performance and ageing manual forecasts."),
  ("Forecast accuracy measurement","systematic comparison of forecasts with actual sales."),
  ("Inbound shipment planning","FBA restock planning, carton allocation and warehouse handover."),
  ("Stock discrepancy detection","identification of differences between booking systems and physical stock."),
  ("Logistics cost tracking","recording and allocation of logistics costs."),
  ("Inventory valuation","monthly valuation of inventory.")],
 [("Backend","Node.js / Express on Google Cloud Run"),("Data","Google BigQuery, PostgreSQL (Supabase)"),
  ("Frontend","Single-page JavaScript application"),("Integrations","Amazon Selling Partner API, Flexport, Acenda, Shopify, product information management (PIM) system")],
 "Approximately 1,300 SKU &times; marketplace combinations across Amazon US, Amazon Canada, Target and Australia.",
 "Developed by Pensero Ltd. In production since March 2026.")

app_page("launch-command-center.html","Launch Command Center",
 "A single cockpit for product launches that brings sales, advertising, rankings and inventory together.",
 ["The Launch Command Center supports the launch and ongoing management of products on Amazon. It combines sales, advertising, keyword ranking and inventory data in one interface, derives data-based recommendations for advertising campaigns and executes approved changes in a controlled and logged way.",
  "It is used in the daily operations of a multi-marketplace Amazon brand."],
 [("Launch tracking","daily units, profit, best-seller rank, keyword ranks, price and advertising metrics per product; flags low stock, falling ranks and products requiring action."),
  ("PPC dashboard","per product, every campaign, keyword, search term and placement with the full change history; budget usage, Brand Analytics search volume and seasonality curves."),
  ("Data-based recommendations","identification of wasted spend, bids with room to decrease, unprofitable placements and converting search terms to harvest; safeguards for new campaigns, cool-down periods and impression-drop checks."),
  ("Controlled execution via AI agents","a change list is prepared, software agents check each change against defined rules, request approval, apply the change and log it."),
  ("Impact measurement","comparison of the 30 days before and after each change: units, profit and rank."),
  ("Promotions and search query opportunities","overview of promotions and opportunities from Search Query Performance data.")],
 [("Data","Google BigQuery, PostgreSQL (Supabase)"),
  ("Integrations","Amazon Ads API, Amazon Brand Analytics, Keepa, DataDive"),
  ("Data refresh","Several times per day")],
 "",
 "Developed by Pensero Ltd. In production since March 2026.")

app_page("sales-performance-dashboard.html","Sales Performance Dashboard",
 "Business intelligence for Amazon sales, from full-funnel metrics to a complete profit and loss statement.",
 ["The Sales Performance Dashboard is a near real-time business intelligence application for Amazon sales, built on Google BigQuery and Google Cloud Run. It tracks sales performance at daily, monthly and product level and breaks results down to individual Amazon fee lines."],
 [("Full-funnel tracking","daily, monthly and per-product figures for units, revenue, sessions, conversion rate, refunds and advertising spend."),
  ("Growth analytics","month-on-month, week-on-week, quarter-on-quarter and year-on-year comparisons, year-, quarter- and month-to-date views over more than three years, with targets and progress tracking."),
  ("Profit and loss","a complete P&amp;L down to every Amazon fee line: referral fees, FBA fees, storage, refund costs, cost of goods and advertising spend."),
  ("Amazon fee monitoring","a fee dashboard with outlier detection, flagging month-on-month increases above 25%."),
  ("Product drill-down","per SKU down to the individual day: trends, best-seller rank, listing-change log, coupons, ratings and reviews."),
  ("Filtering and export","flexible filters, CSV export and role-based access.")],
 [("Platform","Google Cloud Run"),("Data","Google BigQuery"),("Access","Role-based user access")],
 "More than 900 SKUs across Amazon US, Amazon Canada and Target.com.",
 "Developed by Pensero Ltd. In production since April 2026.")

app_page("voice-of-customer-dashboard.html","Voice of Customer Dashboard",
 "An internal application for systematically reducing returns and customer issues on Amazon.",
 ["Returns and refunds reduce margin. Their causes are typically scattered across return reasons, customer comments, reviews and various reports. The Voice of Customer Dashboard consolidates these signals, surfaces the most urgent issues and tracks whether the measures taken are effective."],
 [("Priority list","approximately 275 product families ranked by urgency, with views for quality, listing, logistics and per team member."),
  ("Issue rate","refunds and replacements combined into the actual problem rate per product and variant."),
  ("Customer comment analysis","automatic clustering of comments into problem categories such as quality, product description or transit damage."),
  ("Product detail view","12-week and 12-month trends, price versus returns, conversion versus returns, cost of issues and profit, at parent or variant level."),
  ("Measures log","every product, packaging or listing change is recorded together with the issue rate at that time, so that the effect can be measured before and after."),
  ("Packaging optimisation","analysis of which products should ship in their own packaging and where this is not economical.")],
 [("Data pipelines","Automated pipelines from Amazon data sources"),("Data","Google BigQuery, PostgreSQL (Supabase)"),
  ("Integrations","Product information management (PIM) system, Slack alerts")],
 "",
 "Developed by Pensero Ltd. In production since May 2026.")

# ---------------- About ----------------
about = head("About","Company profile","Pensero Ltd is a private limited company registered in Cyprus. The company provides consulting services to Amazon e-commerce businesses and develops and licenses software applications for e-commerce operations.")
about += f"""<section class="section"><div class="wrap narrow">
<h2 style="margin-top:0">Company details</h2>
<table class="facts"><tbody>
<tr><th scope="row">Company name</th><td>Pensero Ltd</td></tr>
<tr><th scope="row">Registered in</th><td>Republic of Cyprus</td></tr>
<tr><th scope="row">Registration number</th><td>{REGNO}</td></tr>
<tr><th scope="row">Registered office</th><td>{ADDRESS}</td></tr>
<tr><th scope="row">Director</th><td>Eduard Denk</td></tr>
<tr><th scope="row">Areas of activity</th><td>Consulting for Amazon e-commerce businesses; development and licensing of software</td></tr>
</tbody></table>

<h2>Activities</h2>
<p><strong>Consulting.</strong> Pensero Ltd advises businesses selling on Amazon marketplaces on product selection and development, listings, advertising, inventory and logistics, controlling and internal organisation. <a href="consulting.html">Consulting services</a></p>
<p><strong>Software.</strong> Pensero Ltd has developed four web applications for inventory planning, product launches and advertising, sales reporting and customer feedback analysis. The software is licensed to business customers under licence agreements. <a href="software.html">Software applications</a></p>

<h2>Management</h2>
<p>Pensero Ltd was founded by Eduard Denk, who is the company&rsquo;s director. Before founding Pensero Ltd, he was Chief Operating Officer of an Amazon business, with responsibility for operations, sales growth and profitability over a period of three and a half years. He directs the company&rsquo;s consulting activities and the development of its software applications.</p>
<p>Working languages: English and German.</p>
</div></section>"""
page("about.html","About","Company profile of Pensero Ltd, Cyprus.",about,"about.html")

# ---------------- Contact ----------------
contact = head("Contact","Contact")
contact += f"""<section class="section"><div class="wrap narrow">
<table class="facts"><tbody>
<tr><th scope="row">Company</th><td>Pensero Ltd</td></tr>
<tr><th scope="row">Address</th><td>{ADDRESS}</td></tr>
<tr><th scope="row">Email</th><td>{EMAIL}</td></tr>
</tbody></table>
<p>Company and registration details are listed in the <a href="legal-notice.html">Legal Notice</a>.</p>
</div></section>"""
page("contact.html","Contact","Contact details of Pensero Ltd, Cyprus.",contact,"contact.html")

# ---------------- Legal notice ----------------
legal = head("Legal","Legal Notice","Information pursuant to Article 5 of Directive 2000/31/EC (Electronic Commerce Directive) and the corresponding Cypriot legislation.")
legal += f"""<section class="section"><div class="wrap narrow">
<h2 style="margin-top:0">Service provider</h2>
<table class="facts"><tbody>
<tr><th scope="row">Company name</th><td>Pensero Ltd</td></tr>
<tr><th scope="row">Registered office</th><td>{ADDRESS}</td></tr>
<tr><th scope="row">Email</th><td>{EMAIL}</td></tr>
<tr><th scope="row">Director</th><td>Eduard Denk</td></tr>
<tr><th scope="row">Company register</th><td>Department of Registrar of Companies and Intellectual Property, Ministry of Energy, Commerce and Industry, Nicosia</td></tr>
<tr><th scope="row">Registration number</th><td>{REGNO}</td></tr>
<tr><th scope="row">VAT identification number</th><td>CY10421465J</td></tr>
</tbody></table>

<h2>Responsibility for content</h2>
<p>Responsible for the content of this website: Eduard Denk, Director, Pensero Ltd, address as above.</p>

<h2>Liability for content</h2>
<p>The content of this website has been prepared with care. Pensero Ltd does not, however, accept liability for the accuracy, completeness or timeliness of the information provided. The information on this website does not constitute an offer.</p>

<h2>Liability for links</h2>
<p>This website may contain links to external websites. Pensero Ltd has no influence over the content of those websites and accepts no responsibility for them. The respective provider is responsible for the content of linked pages.</p>

<h2>Copyright</h2>
<p>The content of this website and the software applications described on it are protected by copyright. Pensero Ltd is the owner of the rights in the software applications described on this website. Product and company names of third parties (including Amazon) are trademarks of their respective owners; their mention does not imply any affiliation.</p>
</div></section>"""
page("legal-notice.html","Legal Notice","Legal notice of Pensero Ltd, Cyprus.",legal,"")

# ---------------- Privacy ----------------
priv = head("Legal","Privacy Notice","Information on the processing of personal data in accordance with Articles 13 and 14 of the General Data Protection Regulation (EU) 2016/679 (GDPR).")
priv += f"""<section class="section"><div class="wrap narrow">
<p>Last updated: 15 October 2026</p>

<h2>1. Controller</h2>
<p>Pensero Ltd, {ADDRESS}. Email: {EMAIL}.</p>
<p>Pensero Ltd has not appointed a data protection officer, as it is not required to do so.</p>

<h2>2. Summary</h2>
<p>This website is a static website. It does not use cookies, analytics or tracking tools, social media plug-ins, externally loaded fonts or scripts, or contact forms. Personal data is processed only to the extent described below.</p>

<h2>3. Hosting and server log files</h2>
<p>This website is hosted by GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA (GitHub Pages). When the website is accessed, the hosting provider&rsquo;s servers automatically process technical data transmitted by the browser in order to deliver the website and to ensure its security and stability. This may include the IP address, date and time of the request, the page requested, the referring URL, the browser type and version and the operating system.</p>
<p>Legal basis: Article 6(1)(f) GDPR (legitimate interest in the secure and reliable provision of the website). Log data is retained by the hosting provider for a limited period in accordance with the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub Privacy Statement</a> and then deleted. The hosting provider acts as processor on behalf of Pensero Ltd. Where the provider processes data outside the European Economic Area, this is based on an adequacy decision or on standard contractual clauses pursuant to Article 46 GDPR.</p>

<h2>4. Contact by email</h2>
<p>If you contact Pensero Ltd by email, the data you provide (such as your name, email address and the content of your message) is processed in order to deal with your enquiry. Legal basis: Article 6(1)(b) GDPR where the enquiry relates to a contract or pre-contractual measures, otherwise Article 6(1)(f) GDPR (legitimate interest in responding to enquiries). The data is deleted once it is no longer required for this purpose, unless statutory retention obligations apply.</p>

<h2>5. Recipients</h2>
<p>Personal data is not sold or transferred to third parties. Recipients are limited to the hosting provider and the email service provider used by Pensero Ltd (Microsoft Ireland Operations Limited, Microsoft 365), acting as processors, and to authorities where required by law.</p>
<h2>Transfers outside the EU</h2>
<p>GitHub, Inc. is located in the United States and is certified under the EU-U.S. Data Privacy Framework. Transfers are based on the European Commission&rsquo;s adequacy decision of 10 July 2023 (Article 45 GDPR) and, where applicable, standard contractual clauses (Article 46 GDPR).</p>

<h2>6. Your rights</h2>
<p>Under the GDPR you have the right of access (Article 15), rectification (Article 16), erasure (Article 17), restriction of processing (Article 18), data portability (Article 20) and the right to object to processing based on legitimate interests (Article 21). To exercise these rights, please contact Pensero Ltd at the email address above.</p>

<h2>7. Right to lodge a complaint</h2>
<p>You have the right to lodge a complaint with a supervisory authority. The competent authority in Cyprus is the Office of the Commissioner for Personal Data Protection, Nicosia (<a href="https://www.dataprotection.gov.cy">www.dataprotection.gov.cy</a>). You may also contact the supervisory authority in your country of residence.</p>

<h2>8. Changes</h2>
<p>This notice may be updated if the website or the applicable legal requirements change. The current version is published on this page.</p>
</div></section>"""
page("privacy.html","Privacy Notice","Privacy notice of Pensero Ltd for this website.",priv,"")
print("ok")

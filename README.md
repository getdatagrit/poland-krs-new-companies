# Poland KRS New Company Registrations Feed

Newly registered Polish companies, foundations and associations from the official KRS court register: NIP, address, PKD, capital, email, with filters and change detection.

[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-0f9f74)](https://apify.com/datagrit/poland-krs-new-companies) [![Docs](https://img.shields.io/badge/docs-getdatagrit.github.io-0e1726)](https://getdatagrit.github.io/poland-krs-new-companies/)

**from $10.50 per 1,000 results + $10 per run (pay per result; the rate depends on your Apify plan).** Export as JSON, CSV or Excel, call it through the API, or schedule it on Apify.

## What it does

Get a list of Polish companies, foundations and associations that were just registered in the official KRS court register. Every row carries the KRS number, name, legal form, registered address, PKD activity code, share capital and, when the entity published them, an email address, a website, NIP and REGON. It is built for B2B sales teams, accountants, banks, insurers, KYB analysts and service providers who follow new Polish companies from their first days.

Instead of looking up companies one by one by KRS number, you pick a date window and the Actor returns everything first registered in it. You can narrow the feed by legal form, voivodeship, city, activity code, name keyword, share capital, published email and published website.

## Quick start

1. Open [Poland KRS New Company Registrations Feed on Apify Store](https://apify.com/datagrit/poland-krs-new-companies) and click **Try for free**.
2. Fill in the input form (or paste the JSON below) and run it.
3. Download the dataset, or fetch it from the API.

```json
{
  "mode": "newRegistrations",
  "daysBack": 2,
  "scanDepth": "recent",
  "maxItems": 30
}
```

## Input

| Field | Type | What it does |
|---|---|---|
| `mode` | string | "New registrations" returns entities first entered in KRS inside the date window. "All changes" returns every entity that had any entry in the window (new registrations plus changes to existing entities). |
| `daysBack` | integer | How many working days to look back (Monday to Friday, Polish public holidays excluded), counting today when it is a working day. The window runs from the earliest of those days to today, so weekend and holiday entries in between are included. 2 = today and the previous working day; on a Sunday that is Thursday to Sunday, on a Monday Friday to Monday. Maximum 15. Ignored when "From date" is set. |
| `dateFrom` | string | First day of the window, YYYY-MM-DD. The KRS API serves bulletins from January 2020 onwards. Leave empty to use "Working days back". |
| `dateTo` | string | Last day of the window, YYYY-MM-DD (inclusive). Defaults to today. This Actor accepts windows of at most 31 days; split longer periods into several runs. |
| `registers` | array | "P" is the register of entrepreneurs (companies, partnerships, cooperatives). "S" is the register of associations, foundations and other social organisations. Use ["P","S"] for both. |
| `scanDepth` | string | "Complete" reads every entity with an entry in the window whose KRS number is among the newest 100,000 numbers in that window's bulletins (in "All changes" mode: every entity with an entry). New registrations get numbers close to the newest ones: on the fully read days 2026-09-25 and 2026-09-29, 575 of the 576 entities with a registration date on that day were within the newest 16,431 numbers; the exception was an entity with a number more than 500,000 below the newest and 21 register entries. "Recent" reads only the newest 3,000 numbers: much faster, and it returned 261 of the 267 registrations of 2026-09-29. |
| `legalForms` | array | Keep only these legal forms. Allowed: llc, joint-stock, simple-joint-stock, general-partnership, limited-partnership, limited-joint-stock-partnership, professional-partnership, foundation, association, cooperative, other. |
| `voivodeships` | array | Keep only entities with the registered seat in these voivodeships, for example MAZOWIECKIE or Łódzkie (case and Polish letters do not matter). |
| `cities` | array | Keep only entities whose address is in one of these cities, for example Warszawa or Kraków. |
| `pkdPrefixes` | array | Keep only entities whose activity code starts with one of these prefixes, for example 62 (IT), 62.01 or 47.91.Z. Which codes are checked depends on "PKD scope". |
| `pkdScope` | string | "Main" matches only the predominant activity. "Any" also matches the additional activities listed in the register. |
| `nameKeywords` | array | Keep only entities whose name contains at least one of these words, for example software or transport. Case and Polish letters do not matter. |
| `minShareCapital` | number | Keep only entities with a share capital of at least this amount. Entities without a capital (associations, partnerships) are dropped when this is set. |
| `maxShareCapital` | number | Keep only entities with a share capital of at most this amount. Entities without a capital are dropped when this is set. |
| `onlyWithEmail` | boolean | Return only entities that published an email address in the register. |
| `onlyWithWebsite` | boolean | Return only entities that published a website address in the register. |
| `sinceLastRun` | boolean | Skip entities that earlier runs with the same settings already returned. The state is kept per combination of mode, registers, scan depth and all filters (the date window and "Maximum companies" do not count), in a key-value store named krs-feed-state in your account, for 45 days (35 in "All changes" mode). Only entities actually returned to you are remembered. Runs with other filters, and manual test runs with other settings, do not affect it. |
| `maxItems` | integer | Stop after this many entities. Also caps what the run can cost: you pay per entity returned. |
| `proxyConfiguration` | object | The official KRS API is public and needs no proxy. Enable one only if your runs are blocked. |

## Output

| Field | Type | Description |
|---|---|---|
| `krs` | string | Ten-digit KRS number, the primary key of the entity. |
| `register` | string | P = register of entrepreneurs, S = register of associations and foundations. |
| `name` | string | Registered name of the entity. |
| `legalForm` | string | Legal form as written in the register (Polish). |
| `legalFormType` | string | Normalised legal form: llc, joint-stock, simple-joint-stock, general-partnership, limited-partnership, limited-joint-stock-partnership, professional-partnership, foundation, association, cooperative or other. |
| `nip` | string | Ten-digit Polish tax number. Often null for entities registered in the last days. |
| `regon` | string | Nine- or fourteen-digit statistical number. Often null for entities registered in the last days. |
| `registrationDate` | string | Date of the first KRS entry, YYYY-MM-DD. |
| `isNewRegistration` | boolean | True when the registration date falls inside the requested date window; false for existing entities returned in "All changes" mode. |
| `lastEntryDate` | string | Date of the most recent KRS entry, YYYY-MM-DD. |
| `lastEntryNumber` | integer | Sequence number of the most recent entry. |
| `street` | string | Street of the registered seat. |
| `buildingNumber` | string | Building number of the registered seat. |
| `unitNumber` | string | Unit or office number of the registered seat. |
| `postalCode` | string | Postal code of the registered seat. |
| `city` | string | City of the registered seat address. |
| `municipality` | string | Gmina of the seat. |
| `county` | string | Powiat of the seat. |
| `voivodeship` | string | Voivodeship of the seat, uppercase Polish name. |
| `country` | string | Country of the address. |
| `email` | string | Email address published in the register, lowercase, exactly as the entity entered it (for small companies it can contain the name of a person). Null when the entity did not publish one. |
| `website` | string | Website address published in the register, with the host in lowercase. Null when missing or not a valid address. |
| `shareCapital` | number | Share capital (or fund capital) amount. Null for entities without one, such as associations and most partnerships. |
| `capitalCurrency` | string | Currency of the share capital. |
| `mainPkdCode` | string | Predominant activity in the Polish PKD classification. |
| `mainPkdDescription` | string | Polish description of the predominant activity. |
| `additionalPkdCodes` | array | Other declared activities, deduplicated. |
| `boardBodyName` | string | Name of the body that represents the entity, for example ZARZĄD. |
| `boardMembersCount` | integer | Number of people in the representing body. Names are masked by the register, so only the count is returned. |
| `supervisoryBoardMembersCount` | integer | Number of people in supervisory bodies (null when the entity has none). |
| `representationRule` | string | Rule describing who may represent the entity, in Polish. |
| `shareholdersCount` | integer | Number of shareholders or partners listed. Names are masked, so only the count is returned. |
| `soleOwner` | boolean | True when one shareholder owns all shares. |
| `sourceUrl` | string | Official KRS API address of the extract this row was built from. |
| `found` | boolean | True for a real entity; false for the single status row returned when nothing matched. |
| `scrapedAt` | string | Time the row was produced, ISO 8601. |

Sample record:

```json
{
  "krs": "0001269391",
  "register": "P",
  "name": "LEARNLY SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ",
  "legalForm": "SPÓŁKA Z OGRANICZONĄ ODPOWIEDZIALNOŚCIĄ",
  "legalFormType": "llc",
  "nip": "5252999999",
  "regon": "389999999",
  "registrationDate": "2026-09-29",
  "isNewRegistration": true,
  "lastEntryDate": "2026-09-29",
  "lastEntryNumber": 1,
  "street": "ul. Przykładowa",
  "buildingNumber": "12",
  "unitNumber": "4",
  "postalCode": "70-001",
  "city": "SZCZECIN",
  "municipality": "M. SZCZECIN",
  "county": "SZCZECIN",
  "voivodeship": "ZACHODNIOPOMORSKIE",
  "country": "POLSKA",
  "email": "kontakt@example.pl",
  "website": "example.pl",
  "shareCapital": 5000,
  "capitalCurrency": "PLN",
  "mainPkdCode": "85.59.B",
  "mainPkdDescription": "POZOSTAŁE POZASZKOLNE FORMY EDUKACJI, GDZIE INDZIEJ NIESKLASYFIKOWANO",
  "additionalPkdCodes": [
    "62.01.Z",
    "63.11.Z"
  ],
  "boardBodyName": "ZARZĄD",
  "boardMembersCount": 2,
  "supervisoryBoardMembersCount": 3,
  "representationRule": "DO SKŁADANIA OŚWIADCZEŃ W IMIENIU SPÓŁKI UPRAWNIONY JEST KAŻDY CZŁONEK ZARZĄDU SAMODZIELNIE",
  "shareholdersCount": 2,
  "soleOwner": false,
  "sourceUrl": "https://api-krs.ms.gov.pl/api/krs/OdpisAktualny/0001269391?rejestr=P&format=json",
  "found": true,
  "scrapedAt": "2026-09-30T08:00:00.000Z"
}
```

## Call it from code

Runnable examples are in [`examples/`](examples). Replace `YOUR_APIFY_TOKEN` with the token from your Apify account settings.

```bash
curl -X POST "https://api.apify.com/v2/acts/datagrit~poland-krs-new-companies/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"mode":"newRegistrations","daysBack":2,"scanDepth":"recent","maxItems":30}'
```


## More from datagrit

- [French Company Finder - Sirene Financials](https://github.com/getdatagrit/french-company-finder) - French company lead lists from Sirene screened by net result and revenue, with net margin, size, matching establishment and optional directors.
- [GLEIF LEI Lookup - Parents And Subsidiaries](https://github.com/getdatagrit/gleif-lei-ownership-tree) - GLEIF legal entity records with direct and ultimate parents, reporting exceptions and direct subsidiaries.
- [IRS 990 Nonprofit Officers and Compensation](https://github.com/getdatagrit/irs-990-officer-compensation) - Named officers, directors and key employees with pay, hours and titles from IRS e-filed 990, 990-EZ and 990-PF returns.
- [TED Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/ted-contract-expiry-radar) - Find EU public contracts approaching expiry from TED award notices: incumbent, buyer, value, end date and renewal options.
- [UK Contract Expiry Radar - Recompete Leads](https://github.com/getdatagrit/uk-contract-expiry-radar) - UK public contracts ending soon with incumbent supplier, buyer, value and contact - recompete leads from Contracts Finder award notices.

All Actors: [https://getdatagrit.github.io/](https://getdatagrit.github.io/) · [Apify Store](https://apify.com/datagrit)

---

This repository holds documentation and usage examples. Questions, bug reports and feature requests: use the **Issues** tab of the Actor page on [Apify Store](https://apify.com/datagrit/poland-krs-new-companies). Examples are MIT licensed.

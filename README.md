# Cat Health Dashboard (Monet & Maya)

A self-hosted, sensor-driven health monitoring system for our cats **Monet** and **Maya**. The goal is to establish a **baseline** for normal daily behavior (litterbox use, eating, drinking) and then detect meaningful deviations that could indicate health concerns.

---

## Why we built this

Cats are great at hiding illness. Small changes in routine can be early warning signs, for example:

- **Drinking more** → possible kidney issues, diabetes, hyperthyroidism  
- **Urinating more often** → possible UTI, stress, urinary crystals  
- **Not pooping / reduced output** → possible constipation or intestinal blockage  
- **Changes in eating patterns** → illness, dental issues, stress  

This project helps us quantify “normal” for each cat and receive alerts when patterns shift.

---

## Project goals

1. **Collect** litterbox, eating, and drinking activity data automatically (via sensors).
2. **Store** events in a structured SQL database.
3. **Clean & validate** data for reliable analysis (deduping, timestamps, missing values).
4. **Analyze** behavior trends and compute daily/weekly statistics.
5. **Model** expected behavior and detect anomalies (per-cat baselines).
6. **Visualize** activity in a web dashboard and **notify** us if metrics drift.

---

## High-level system overview

### Data pipeline (Marita Scope)

1. **Data collection**
   - Ingest events from sensors (and/or manual logs during early testing).
   - Standardize timestamps and event formats.

2. **Storage**
   - Write events to SQL tables (litterbox, eating, drinking).
   - Enforce consistent schemas and relationships.

3. **Cleaning & quality checks**
   - Deduplicate events
   - Validate ranges (e.g., duration not negative, timestamps not in the future)
   - Normalize categorical values (e.g., `waste_type`, `food_type`, `source`)

4. **Analysis**
   - Daily aggregates (per cat):
     - litterbox counts by waste type
     - total time in litterbox
     - number of eating events + total grams
     - number of drinking events + total mL
   - Trend windows:
     - last 7 days vs last 30 days vs baseline
   - Time-of-day patterns (optional)

5. **Modeling & alerts**
   - Establish **baseline** distributions for each cat (rolling or fixed baseline)
   - Detect anomalies (examples):
     - drinking mL/day above baseline threshold
     - urination frequency spikes
     - no poop events in X hours
   - Produce alert flags + severity scores for dashboard/notifications

### Hardware + hosting (Mars Scope)

- Sensor architecture and event generation
- SQL Server setup and administration
- Web server + dashboard application
- Self-hosting infrastructure:
  - accessible outside our home network (securely)
  - reliable uptime and backups

---

## Database design

### Entities

- **cats**: one record per cat (Monet, Maya)
- **litterbox_events**: one record per litterbox visit
- **eating_events**: one record per eating event
- **drinking_events**: one record per drinking event

### Relationships

All event tables link back to `cats`:

- `cats (1) → (many) litterbox_events`
- `cats (1) → (many) eating_events`
- `cats (1) → (many) drinking_events`

### Schema (conceptual)

**cats**
- `cat_id` (PK)
- `name`
- optional metadata: `sex`, `birthdate`, `notes`

**litterbox_events**
- `litter_event_id` (PK)
- `cat_id` (FK → cats)
- `event_ts`
- `duration_seconds`
- `waste_type` (VARCHAR)
- `notes`

**eating_events**
- `eating_event_id` (PK)
- `cat_id` (FK → cats)
- `event_ts`
- `food_type` (VARCHAR)
- `amount_grams`
- `notes`

**drinking_events**
- `drinking_event_id` (PK)
- `cat_id` (FK → cats)
- `event_ts`
- `water_ml`
- `duration_seconds`
- `source` (VARCHAR)
- `notes`

---

## Dashboard outputs (planned)

Per cat (Monet / Maya), show:

- **Today / 7-day / 30-day** summaries
- Drinking (mL/day) trend line + anomaly markers
- Urination frequency trend + anomaly markers
- Poop frequency + “time since last poop”
- Eating frequency + grams/day
- Alerts panel with reasons + timestamps

---

## Alert examples (rules + modeled)

We plan to support both rule-based alerts and learned baselines.

### Rule-based
- No poop in last `X` hours
- Urination count ≥ `N` in last 24 hours
- Drinking mL/day exceeds a fixed threshold

### Baseline/anomaly-based
- Drinking mL/day > baseline mean + k·std (or percentile-based)
- Poop frequency drops below baseline percentile
- Change-point detection on daily totals

---

## Security & access

This is a **self-hosted** system, accessible outside our home network. We plan to prioritize:

- authentication for dashboard access
- encrypted transport
- restricted network exposure
- regular backups of the SQL database

---

